N=int(input())
s=[]
for i in range(N):
    s.append(input())
M=int(input())
t=[]
for i in range(M):
    t.append(input())
wordlist=list(set(s))+list(set(t))
wordcount=[]
for i in range(len(wordlist)):
    wordcount.append(s.count(wordlist[i])-t.count(wordlist[i]))
if max(wordcount)>=1:
    print(max(wordcount))
else:
    print(0)
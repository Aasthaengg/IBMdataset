S=input()
d=[[-1,len(S)] for i in range(26)]
for i,s in enumerate(S):
    d[ord(s)-ord('a')].insert(-1,i)
print(min([max([l[i+1]-l[i]-1 for i in range(len(l)-1)]) for l in d]))
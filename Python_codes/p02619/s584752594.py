d = int(input())
c = list(map(int,input().split()))
like=0
but=0
s=[]
last=[]
for i in range(26):
    last.append(0)
for i in range(d):
    keys=list(map(int,input().split()))
    s.append(keys)
t=[]
for i in range(d):
    t.append(int(input())-1)
for i in range (d):
    like+=s[i][t[i]]
    #print(like)
    last[t[i]]=i+1
    for j in range(26):
        like-=c[j]*(i+1-last[j])
    print(like)
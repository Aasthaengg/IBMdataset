N=int(input())
s=[]
for i in range(N):
    s.append(str(input()))
M=int(input())
t=[]
for j in range(M):
    t.append(str(input()))

ans=0
for i in range(N):
    x=s.count(s[i])
    y=t.count(s[i])
    if ans<x-y:
        ans=x-y
print(ans)
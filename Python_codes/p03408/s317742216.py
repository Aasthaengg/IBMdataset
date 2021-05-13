N=int(input())
ans=0
s=[]
t=[]
for i in range(N):
    s.append(input())
M=int(input())
for j in range(M):
    t.append(input())

s.sort()
t.sort()
for i in range(N-1):
    if s[i]!=s[i+1]:
        sf=s.count(s[i+1])
        tf=t.count(s[i+1])
        if sf>tf:
            temp=sf-tf
            if temp>ans:
                ans=temp
sf=s.count(s[0])
tf=t.count(s[0])
if sf>tf:
    temp=sf-tf
    if ans<temp:
        ans=temp
print(ans)

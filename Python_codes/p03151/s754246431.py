n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
pos,neg=[],0
if sum(a)<sum(b):print(-1);exit()
ne=0
for i in range(n):
    if a[i]==b[i]:continue
    if a[i]<b[i]:neg+=-a[i]+b[i];ne+=1
    else:pos.append(a[i]-b[i])
s=0
pos.sort(reverse=1)
ans=0


for i in pos:
    if s>=neg:print(ans+ne);exit()
    s+=i
    ans+=1

print(ans+ne)
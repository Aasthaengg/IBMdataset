import collections

N=int(input())
check1=list()
for i in range(N):
  check1.append(int(input()))
c=collections.Counter(check1)
check2=set(check1)
ans=0
for i in check2:
  if c[i]%2!=0:
    ans+=1
print(ans)

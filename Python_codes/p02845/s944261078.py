n=int(input())
a=list(map(int,input().split()))
m=10**9+7
b=[0]*3
ans=1
for i in a:
  ans*=b.count(i)
  ans%=m
  for j in range(3):
    if b[j]==i:
      b[j]+=1
      break
print(ans%m)
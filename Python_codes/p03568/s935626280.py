N=int(input())
A=list(map(int,input().split()))
ans=3**N
tmp=1
for i in A:
  if i%2==0:
    tmp*=2
ans-=tmp
print(ans)
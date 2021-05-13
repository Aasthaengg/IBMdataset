A,B=map(int,input().split())

ans=0
for _ in range(2):
  if A<B:
    temp=B
    B-=1
  else:
    temp=A
    A-=1
  ans+=temp

print(ans)

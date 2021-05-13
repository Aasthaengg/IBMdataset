N,X=map(int,input().split())
s=0
m=X
for i in range(N):
  a=int(input())
  s+=a
  if a<m:
    m=a
print(N+(X-s)//m)
n,m,c=map(int,input().split())
b_list=list(map(int,input().split()))

ans=0
for i in range(n):
  a_list=list(map(int,input().split()))
  num=0
  for j in range(m):
    num+=b_list[j]*a_list[j]
  if num+c>0:
    ans+=1

print(ans)
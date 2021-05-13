n,x=map(int,input().split())
a=[]
for i in range(n):
  a.append(int(input()))
s=x-sum(a)
ans=s//min(a)+n
print(ans)
n,m,c=map(int,input().split())
b=list(map(int,input ().split()))
num=0
for _ in range(n):
  a=list(map(int,input().split()))
  hoge=0
  for i in range(m):
    hoge+=a[i]*b[i]
  if hoge+c>0:
    num+=1
print(num)
n,m,c=map(int,input().split())
b=list(map(int,input().split()))
count=0
for _ in range(n):
  result=c
  a=list(map(int,input().split()))
  for i,j in zip(a,b):
    result+=i*j
  if result>0: count+=1
print(count)
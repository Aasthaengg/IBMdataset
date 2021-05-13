n,m=map(int,input().split())
x=[]
sum=0
for i in range(n):
  s=list(map(int,input().split()))
  s.pop(0)
  x+=s
for j in range(1,m+1):
  if x.count(j)==n:
    sum+=1
print(sum)

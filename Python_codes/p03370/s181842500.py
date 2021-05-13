n,m=map(int, input().split())
min=1000000000
sum=0
for i in range(n):
  j=int(input())
  if min>j:
    min=j
  m-=j
  sum+=1
print(sum+m//min)
n=int(input())
t=list(map(int, input().split()))
m=int(input())
for i in range(m):
  p,x=map(int, input().split())
  time=0
  for j in range(n):
    if j==p-1:
      time+=x
    else:
      time+=t[j]
  print(time)
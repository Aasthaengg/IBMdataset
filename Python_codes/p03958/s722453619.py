k,t=map(int,input().split())
a=list(map(int,input().split()))
a_m=0
sm =0
for i in range(1,t):
  if a[a_m] < a[i]:
    sm += a[a_m]
    a_m = i
  else:
    sm += a[i]

print(max(0, a[a_m]-sm-1))
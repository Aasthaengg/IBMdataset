n=int(input())
a=[0]+list(map(int,input().split()))+[0]
cum_a=[0]*(n+2)
for i in range(n+1):
  cum_a[i+1]=cum_a[i]+abs(a[i+1]-a[i])
for i in range(n):
  print(cum_a[n+1]-abs(a[i+1]-a[i])-abs(a[i+2]-a[i+1])+abs(a[i+2]-a[i]))
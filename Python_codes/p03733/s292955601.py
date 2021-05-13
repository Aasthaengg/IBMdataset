n,m = map(int,input().split())
t = list(map(int,input().split()))
time = 0
for i in range(1,n):
  time+=min(m,t[i]-t[i-1])
time+=m
print(time)
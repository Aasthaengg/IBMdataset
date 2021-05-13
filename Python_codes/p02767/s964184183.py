n=int(input())
x=list(map(int,input().split()))

health = 10**9
p_min = min(x)
p_max = max(x)
for p in range(p_min,p_max+1):
  tmp = 0
  for i in range(n):
    tmp += (x[i]-p)**2
    
  health = min(health, tmp)
print(health)
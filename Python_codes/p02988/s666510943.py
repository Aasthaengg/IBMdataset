n = int(input())
p = list(map(int, input().split()))
ans = 0
li = []

for i in range(1, n-1):
  mn = min(p[i-1], p[i], p[i+1])
  mx = max(p[i-1], p[i], p[i+1])
  if p[i]!=mn and p[i]!=mx:
    ans += 1
    
print(ans)
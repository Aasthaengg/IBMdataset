n = int(input())
h = list(map(int,input().split()))
count = 0
ans = 0

for i in range(n):
  if i == n-1 :
    ans = max(ans,count)
    count = 0
  elif h[i] >= h[i+1]:
    count += 1
  else:
    ans = max(ans,count)
    count = 0

print(ans)
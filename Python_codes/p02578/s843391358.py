n = int(input())
L = list(map(int,input().split()))
m = L[0]
ans = 0

for l in L:
  if m == l: 
    continue
  elif m > l: 
    ans += (m - l)
  elif m < l:
    m = l
print(ans)
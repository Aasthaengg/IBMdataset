import bisect
n, x = map(int, input().split())
L = list(map(int, input().split()))
D = [0]
ans = 1
for i in range(1, n+1):
  d = D[i-1] + L[i-1]
  D.append(d)
  if d <= x:
    ans += 1
  else:
    break
print(ans)
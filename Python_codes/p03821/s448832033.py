n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
 
a.reverse()
b.reverse()
ans = 0
 
for j in range(n):
  a[j] += ans
  if a[j] % b[j] != 0:
    ans += b[j] -(a[j] % b[j])
 
print(ans)
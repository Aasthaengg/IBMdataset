n = int(input())
x = [0]*n
y = [0]*n
for i in range(n-1, -1, -1):
  a,b = map(int, input().split())
  x[i] = a
  y[i] = b

ans = 0
for i in range(n):
  if (x[i]+ans) % y[i] != 0:
    ans += y[i]-(x[i]+ans)%y[i]
print(ans)
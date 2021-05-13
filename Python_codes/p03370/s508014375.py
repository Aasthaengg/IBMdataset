n, x = map(int, input().split())
m = [int(input()) for i in range(n)]
sum = 0
mi = 10000

for i in m:
  sum += i
  mi = min(mi, i)

ans = n
x -= sum
ans += x // mi
print(ans)
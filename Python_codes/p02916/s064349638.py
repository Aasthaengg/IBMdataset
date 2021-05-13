n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
bf = 0
for i in range(n):
  eat = a[i]
  ans += b[eat - 1]
  if bf > 0:
    if bf + 1 == eat:
      ans += c[bf - 1]
  bf = eat
print(ans)
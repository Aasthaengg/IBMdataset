n = int(input())
a = [int(input()) for _ in range(n)]
ans = 1
next = a[0]
while True:
  if next == 1:
    ans = -1
    break
  elif next == 2:
    break
  cur = next
  next = a[next - 1]
  a[cur - 1] = 1
  ans += 1
print(ans)
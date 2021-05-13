n = int(input())
a = [int(input())-1 for _ in range(n)]

now = 0
judge = False
ans = 0
for i in range(n):
  ans += 1
  if a[now] == now:
    break
  if a[now] == 1:
    judge = True
    break
  now = a[now]

print(ans if judge else -1)
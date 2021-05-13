N = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
  if a[i] != "": n = a[i] - 1
  if a[n] == i + 1:
    ans += 1
    a[n] = ""
print(ans)
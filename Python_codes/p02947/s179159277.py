
n = int(input())
arr = {}
ans = 0
for _ in range(n):
  S = sorted(list(input()))
  s = ''.join(S)
  if s in arr:
    ans += arr[s]
    arr[s] += 1
  else:
    arr[s] = 1
print(ans)
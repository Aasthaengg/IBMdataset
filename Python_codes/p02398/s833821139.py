arr = map(int, raw_input().split())
ans = 0
for x in range(arr[0], arr[1] + 1):
  if arr[2] % x == 0:
    ans += 1

print(ans)
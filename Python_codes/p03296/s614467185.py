n = int(input())
a = list(map(int, input().split()))
ans = 0
check = 0
for i in range(1, n):
  if a[i-1] == a[i] and check == 0:
    ans += 1
    check = 1
  elif a[i-1] == a[i] and check == 1:
    check = 0
  else:
    check = 0
print(ans)

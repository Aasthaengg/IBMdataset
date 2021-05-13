ans = 0
n = int(input().rstrip())
for i in range(1, n):
  ans += (n-1)//i
print(ans)
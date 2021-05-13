N = int(input())
a = list(map(int, input().split()))
ans = 0
for num in range(N):
  if num % 2 == 0 and a[num] % 2 == 1:
    ans += 1
print(ans)
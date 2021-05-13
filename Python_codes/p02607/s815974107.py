n = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A[::2]:
  if a % 2 == 1:
    ans += 1
print(ans)
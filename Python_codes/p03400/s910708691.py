N = int(input())
D, X = map(int, input().split())
ans = X
for i in range(N):
  a = int(input())
  ans += ((D - 1) // a + 1)
print(ans)
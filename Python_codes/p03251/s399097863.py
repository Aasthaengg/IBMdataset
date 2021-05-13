N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x.sort()
y.sort()
ans = "War"

for Z in range(X + 1, Y + 1):
  if x[-1] < Z and y[0] >= Z:
    ans = "No War"

print(ans)

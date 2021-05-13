n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

a, b = max(x), min(y)
for val in range(X+1, Y):
  if a < val <= b:
    print("No War")
    exit(0)
print("War")
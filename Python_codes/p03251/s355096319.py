N, M, X, Y = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

XR = max(xs)
YL = min(ys)

for i in range(X+1, Y+1):
  if XR < i and i <= YL:
    print("No War")
    exit()

print("War")
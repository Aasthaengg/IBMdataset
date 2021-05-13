X = [0 for _ in range(4)]

for _ in range(3):
    a, b = [int(_) for _ in input().split()]
    X[a-1] += 1
    X[b-1] += 1

if max(X) > 2:
    print("NO")
else:
    print("YES")

x = [0, 0, 0, 0]
for i in range(3):
    a, b = [int(_) for _ in input().split()]
    x[a-1] += 1
    x[b-1] += 1

if max(x) <= 2:
    print("YES")
else:
    print("NO")

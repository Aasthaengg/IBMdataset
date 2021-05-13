ab = [0 for _ in range(4)]
for _ in range(3):
    a, b = map(int, input().split())
    ab[a - 1] += 1
    ab[b - 1] += 1
if ab.count(1) == 2 and ab.count(2) == 2:
    print("YES")
else:
    print("NO")
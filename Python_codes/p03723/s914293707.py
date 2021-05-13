A, B, C = map(int, input().split())
res = 0
while True:
    if A%2 + B%2 + C%2 > 0:
        break
    A, B, C = B//2 + C//2, C//2 + A//2, A//2 + B//2
    if A == B and B == C:
        res = -1
        break
    res += 1
print(res)

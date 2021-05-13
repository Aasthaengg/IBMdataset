# A - Cookie Exchanges

A, B, C = map(int, input().split())

ans = 0
while True:
    if A%2 or B%2 or C%2:
        break
    if A == B == C:
        ans = -1
        break
    nA = B//2 + C//2
    nB = A//2 + C//2
    nC = A//2 + B//2
    A = nA
    B = nB
    C = nC
    ans += 1

print(ans)
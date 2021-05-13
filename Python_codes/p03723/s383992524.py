A, B, C = map(int, input().split())

ans = 0
if A&1 or B&1 or C&1:
    print(ans)
    exit(0)

if A == B == C:
    print(-1)
    exit(0)

while True:
    if A&1 or B&1 or C&1:
        break
    nA = B//2 + C//2
    nB = A//2 + C//2
    nC = B//2 + A//2
    ans += 1
    A = nA
    B = nB
    C = nC

print(ans)


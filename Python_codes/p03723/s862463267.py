A, B, C = map(int, input().split())
ans = 0
if A == B and B == C and A%2 == 0:
    print(-1)
else:
    while A%2 == 0 and B%2 == 0 and C%2 == 0:
        ans += 1
        A, B, C = B//2+C//2, A//2+C//2, A//2+B//2
    print(ans) 
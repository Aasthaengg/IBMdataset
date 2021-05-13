A, B, C = map(int, input().split())

if A == B == C and A%2 == 1:
    print('0')
elif A == B == C:
    print('-1')
else:
    ans = 0
    while A%2 == B%2 == C%2 == 0:
        A, B, C = B//2+C//2, A//2+C//2, A//2+B//2
        ans += 1
    print(ans)

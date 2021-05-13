A, B, C = map(int, input().split())

if A % 2 == 1 and B % 2 == 1 and C % 2 == 1:
    print(0)
    exit()
elif A == B and B == C:
    print('-1')
    exit()
else:
    ans = 0
    while A % 2 != 1 and B % 2 != 1 and C % 2 != 1:
        a = B//2+C//2
        b = C//2+A//2
        c = A//2+B//2
        A, B, C = a, b, c
        ans += 1
print(ans)

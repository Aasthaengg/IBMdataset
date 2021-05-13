A, B, C = map(int, input().split())
if (A * B * C) % 2 == 0:
    ans = 0
    print(ans)
else:
    ans = float('inf')
    V = A*B*C
    AB = A*B
    BC = B*C
    CA = C*A
    ans = min(ans, abs((A//2)*BC - ((A//2) + 1)*BC))
    ans = min(ans, abs((B//2)*CA - ((B//2) + 1)*CA))
    ans = min(ans, abs((C//2)*AB - ((C//2) + 1)*AB))
    print(ans)

from fractions import gcd

N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 'IMPOSSIBLE'

if max(A) < M:
    print(ans)
elif M in A:
    ans = 'POSSIBLE'
    print(ans)
else:
    g = A[-1]
    for a in A:
        g = gcd(g, a)
    if M % g == 0:
        ans = 'POSSIBLE'
        print(ans)
    else:
        print(ans)


import sys
import bisect
A, B, Q = map(int, input().split())
S = [int(sys.stdin.readline().rstrip()) for _ in range(A)]
T = [int(sys.stdin.readline().rstrip()) for _ in range(B)]

def solver(S, A, x):
    d = []
    a = bisect.bisect_right(S, x)

    if a == A:
        d.append((-1, x - S[-1]))
    elif a == 0:
        d.append((1, S[0] - x))
    else:
        d.append((-1, x - S[a - 1]))
        d.append((1, S[a] - x))

    return d

for _ in range(Q):
    ans = 0
    x = int(sys.stdin.readline().rstrip())

    d_a = solver(S, A, x)
    d_b = solver(T, B, x)

    ans = 10**15
    for i, j in d_a:
        for k, l in d_b:
            if i == k:
                ans = min(ans, max(j, l))
            else:
                ans = min(ans, j + l + min(j, l))
    print(ans)
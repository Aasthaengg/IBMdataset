import sys
N, M = map(int, input().split())
A = set(int(sys.stdin.readline()) for _ in range(M))
MOD = 10 ** 9 + 7

ans = 0
if N == 1:
    ans = 1
elif N == 2:
    if M == 0:
        ans = 2
    else:
        ans = 1
else:
    if 1 in A:
        p2 = 0
    else:
        p2 = 1
    if 2 in A:
        p1 = 0
    else:
        p1 = p2 + 1
    for i in range(3, N + 1):
        if i in A:
            p2 = p1
            p1 = 0
        else:
            c = (p1 + p2) % MOD
            p2 = p1
            p1 = c
    ans = p1
print(ans)
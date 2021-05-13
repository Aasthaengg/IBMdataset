# E - Multiplication 4
import heapq
N, K = map(int, input().split())
A = list(int(a) for a in input().split())
MOD = 10**9 + 7


if N == K:
    ans = 1
    for a in A:
        ans = (ans * a) % MOD
else:
    pos = []
    neg = []
    for a in A:
        if a >= 0:
            pos.append(a)
        else:
            neg.append(a)

    if len(neg) == N and K&1 == 1:
        neg.sort(reverse=True)
        ans = 1
        for i in range(K):
            ans = (ans * neg[i]) % MOD
    else:
        pos.sort(reverse=True)
        dbl = []
        ans = 1
        ini = 0
        rem = K
        if K&1 == 1:
            ans = (ans * pos[0]) % MOD
            ini = 1
            rem -= 1
        for i in range(0, (len(pos)-ini)//2):
            heapq.heappush(dbl, (pos[ini+i*2] * pos[ini+i*2+1])*-1)
        neg.sort()
        for i in range(0, len(neg)//2):
            heapq.heappush(dbl, (neg[i*2] * neg[i*2+1]) * -1)
        while rem > 0:
            ans = (ans * heapq.heappop(dbl) * -1) % MOD
            rem -= 2

print(ans)
from collections import defaultdict, deque
import sys
input=sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    MOD = 10**9+7

    d = defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)

    ans = K
    q = deque([1])
    used = [False]*(N+1)
    used[1] = True

    while q:
        s = q.popleft()
        pos = 1 if s==1 else 2
        for t in d[s]:
            if used[t]:continue
            used[t] = True
            ans *= (K-pos)
            ans %= MOD
            pos += 1
            q.append(t)

    print(ans)


if __name__ == "__main__":
    solve()

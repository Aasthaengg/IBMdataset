import sys
sys.setrecursionlimit(10**6)
def main():
    N, K = map(int, input().split())
    Nodes = [set() for _ in range(N)]
    MOD = 10 ** 9 + 7
    for i in range(N - 1):
        a, b = map(int, input().split())
        Nodes[a - 1].add(b - 1)
        Nodes[b - 1].add(a - 1)
    def helper(n, k, f):
        l = len(Nodes[n])
        r = (K - k) 
        j = 1 if k == 0 else 2
        for i in Nodes[n]:
            if i == f:
                continue
            r = r * helper(i, j, n) % MOD
            j += 1
        return r
    for i in range(N):
        if len(Nodes[i]) == 1:
            break
    return helper(i, 0, -1)

print(main())

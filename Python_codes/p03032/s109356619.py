import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(K+1):
        for r in range(K-l+1):
            if l+r > N or l+r>K:
                continue
            now = []
            val = 0
            for i in range(l):
                now.append(V[i])
                val += V[i]
            for j in range(r):
                now.append(V[-j-1])
                val += V[-j-1]

            d = K-l-r
            now.sort()
            for i in range(d):
                if i >= len(now):
                    break
                if now[i] > 0:
                    break
                val -= now[i]
            ans=max(ans,val)

    print(ans)

resolve()
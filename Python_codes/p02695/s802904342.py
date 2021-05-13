import sys
sys.setrecursionlimit(10**9)
N, M, Q = map(int, input().split())
l = []
for _ in range(Q):
    l.append(list(map(int, input().split())))
ans = 0
def dfs(n):
    if len(n) == N+1:
        global ans
        tmp = 0
        for i in range(Q):
            abi = n[l[i][1]]
            aai = n[l[i][0]]
            c = l[i][2]
            d = l[i][3]
            if abi -aai == c:
                tmp += d
        ans = max(ans, tmp)
    else:
        for i in range(n[-1], M+1):
            tmp2 = n[:]
            tmp2.append(i)
            dfs(tmp2)
dfs([1])
print(ans)

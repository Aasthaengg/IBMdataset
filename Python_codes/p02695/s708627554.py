import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**6)

def score(Ans):
    t = 0
    for ai,bi,ci,di in zip(A,B,C,D):
        if Ans[bi]-Ans[ai]==ci:
            t += di
    return t

def dfs(Ans):
    if len(Ans)==n:
        return score(Ans)
    ans = 0
    prev_last = Ans[-1] if len(Ans)>0 else 0
    for v in range(prev_last, m):
        Ans.append(v)
        ans = max(ans, dfs(Ans))
        Ans.pop()
    return ans

n, m, q = map(int, readline().split())
A,B,C,D = [0]*q, [0]*q, [0]*q, [0]*q
for i in range(q):
    a,b,C[i],D[i] = map(int, readline().split())
    A[i] = a-1
    B[i] = b-1

print(dfs([]))
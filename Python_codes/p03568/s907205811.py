from functools import reduce
def solve():
    N = int(input())
    A = list(map(int,input().split()))

    diffs_perm = []
    dfs(list(),N,diffs_perm)

    cnt = 0
    for p in diffs_perm:
        B = A[:]
        for i in range(N):
            B[i] += p[i]
        
        if reduce(lambda a,b:a*b, B) % 2 == 0:
            cnt += 1
    
    print(cnt)

def dfs(diffs,N,res):
    if len(diffs) == N:
        res.append(diffs)
        return
    dfs(diffs[:]+[1],N,res)
    dfs(diffs[:]+[0],N,res)
    dfs(diffs[:]+[-1],N,res)


if __name__ == '__main__':
    solve()
from itertools import accumulate
def solve():
    N,M,Q = map(int,input().split())
    cnt = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        l,r = map(int,input().split())
        cnt[l][r] += 1
    
    acc = []
    for i in range(N+1):
        acc.append(list(accumulate(cnt[i])))
    
    answers = []
    for _ in range(Q):
        p, q = map(int,input().split())
        ans = 0
        for l in range(p, q+1):
            ans += acc[l][q] - acc[l][p-1]
    
        answers.append(ans)

    print(*answers, sep='\n')

if __name__ == '__main__':
    solve()
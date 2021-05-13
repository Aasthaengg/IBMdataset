def solve():
    N = int(input())
    F = []
    for _ in range(N):
        f = list(map(int,input().split()))
        F.append(f)
    
    P = []
    for _ in range(N):
        p = list(map(int,input().split()))
        P.append(p)
    
    ans = -float('inf')
    for i in range(1, 1 << 10):
        me = [0] * 10
        for j in range(10):
            if (i >> j) & 1:
                me[j] = 1

        c = []
        for j in range(N):
            cnt = 0
            for k in range(10):
                if F[j][k] == 1 and me[k] == 1:
                    cnt += 1
            
            c.append(cnt)
        
        now = 0
        for j in range(N):
            now += P[j][c[j]]
        
        ans = max(ans, now)
    
    print(ans)
    
if __name__ == '__main__':
    solve()

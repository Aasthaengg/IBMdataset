from math import ceil
def solve():
    N = int(input())
    A = list(map(int,input().split()))

    mx = [0] * (N+1)
    mn = [0] * (N+1)

    mx[-1] = A[-1]
    mn[-1] = A[-1]

    for i in range(N-1,-1,-1):
        mx[i] = mx[i+1] + A[i]      
        mn[i] = ceil(mn[i+1]/2) + A[i]
    
    if not mn[0] <= 1 <= mx[0]:
        print(-1)
        return

    ans = 1
    now = 1
    piyo = [1]
    for i in range(1,N+1):
        nxt = (now-A[i-1]) * 2
        piyo.append(nxt)
        ans += min(mx[i],nxt)
        now = nxt

    print(ans)
    
if __name__ == '__main__':
    solve()
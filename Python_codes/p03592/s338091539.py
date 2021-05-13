def solve():
    H,W,K = map(int,input().split())

    for k in range(0,H+1):
        for l in range(0,W+1):
            if k*(W-l)+l*(H-k) == K:
                print('Yes')
                return
    else:
        print('No')
if __name__ == '__main__':
    solve()
import sys
from collections import deque
def main():
    MOD=10**9+7
    q=deque()
    H,W=tuple(map(int,sys.stdin.readline().split()))
    m,dp=[],[[0 for _ in range(W)] for _ in range(H)]
    for _ in range(H):m.append(list(sys.stdin.readline().strip()))
    dp[0][0]=1
    q.append((0,0))
    while len(q)>0:
        h,w=q.popleft()
        if h+1<H and m[h+1][w]=='.':  # down
            if dp[h+1][w]==0:q.append((h+1,w))
            dp[h+1][w]=(dp[h+1][w]+dp[h][w])%MOD
        if w+1<W and m[h][w+1]=='.':  # right
            if dp[h][w+1]==0:q.append((h,w+1))
            dp[h][w+1]=(dp[h][w+1]+dp[h][w])%MOD
    print(dp[H-1][W-1])
if __name__=='__main__':main()
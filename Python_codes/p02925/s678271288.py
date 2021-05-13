import sys
input = sys.stdin.buffer.readline
from collections import deque

def main():
    N = int(input())
    memo = []
    base = 0
    for i in range(N-1):
        memo.append(base)
        base += N-i-1
    edge = [[] for _ in range((N*(N-1))//2)]
    IN = [0]*((N*(N-1))//2)
    
    for i in range(N):
        a = list(map(int,input().split()))
        b = []
        for j in a:
            j -= 1
            if i < j:
                b.append(memo[i]+j-i-1)
            else:
                b.append(memo[j]+i-j-1)
        for i in range(N-2):
            edge[b[i]].append(b[i+1])
            IN[b[i+1]] += 1

    def t_sort():
        que = deque([i for i,c in enumerate(IN) if c == 0])
        l = []
        while que:
            now = que.popleft()
            l.append(now)
            for fol in edge[now]:
                IN[fol] -= 1
                if IN[fol] == 0:
                    que.append(fol)
        if len(l) != (N*(N-1))//2:
            print(-1)
            exit()
        return l
    
    ts = t_sort()
    dp = [1]*((N*(N-1))//2)
    for now in ts:
        for fol in edge[now]:
            dp[fol] = max(dp[fol],dp[now]+1)
    
    print(max(dp))

if __name__ == "__main__":
    main()
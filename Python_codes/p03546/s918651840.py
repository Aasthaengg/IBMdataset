import sys
import collections

sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

def dfs(n, used, cost):
    global c, mincost
    for i in range(10):
        if i == 1:
            if cost + c[n][i] < mincost:
                mincost = cost + c[n][i]
                continue
        if i not in used and cost < mincost:
            dfs(i, used+[i], cost+c[n][i])

def main():
    global c, mincost
    H, W = map(int, readline().split())
    c = []
    for _ in range(10):
        c.append(list(map(int, readline().split())))
    wall = []
    wallcount = collections.Counter([])
    for _ in range(H):
        tmp = list(map(int, input().split()))
        wall.append(tmp)
        wallcount += collections.Counter(tmp)
    
    wallitem = list(zip(*wallcount.items()))
    ans = 0
    for i, item in enumerate(wallitem[0]):
        if item in [-1, 1]:
            continue
        mincost = c[item][1]
        dfs(item, [item], 0)
        ans += mincost*wallitem[1][i]
    print(ans)

if __name__ == "__main__":
    main()

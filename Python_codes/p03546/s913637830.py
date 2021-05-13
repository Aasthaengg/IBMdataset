import sys
import collections

sys.setrecursionlimit(10**6)
readline = sys.stdin.readline


def main():
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
    
    for k in range(10):
        for i in range(10):
            for j in range(10):
                c[i][j] = min(c[i][k] + c[k][j], c[i][j])
    
    ans = 0
    for item in wallitem[0]:
        if item in [-1, 1]:
            continue
        ans += wallcount[item]*c[item][1]

    print(ans)

if __name__ == "__main__":
    main()

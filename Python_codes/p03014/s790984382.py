import sys
sys.setrecursionlimit(10**9)

def main():
    H,W = map(int,input().split())
    graph = [[""]*W for _ in range(H)]

    for h in range(H):
        graph[h] = list(input())

    left = [[1]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if graph[h][w] == "#":
                left[h][w] = 0
            else:
                if w-1 >= 0:
                    left[h][w] = left[h][w-1] + 1

    right = [[1]*W for _ in range(H)]
    for h in range(H):
        for w in reversed(range(W)):
            if graph[h][w] == "#":
                right[h][w] = 0
            else:
                if w+1<W:
                    right[h][w] = right[h][w+1] + 1

    down = [[1]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if graph[h][w] == "#":
                down[h][w] = 0
            else:
                if h-1>=0:
                    down[h][w] = down[h-1][w] + 1

    up = [[1]*W for _ in range(H)]
    for h in reversed(range(H)):
        for w in range(W):
            if graph[h][w] == "#":
                up[h][w] = 0
            else:
                if h+1<H:
                    up[h][w] = up[h+1][w] + 1

    ans = 0
    for h in range(H):
        for w in range(W):
            ans = max(ans,up[h][w] + down[h][w] + left[h][w] + right[h][w] - 3)


    print(ans)
    # print(up,"\n",down,"\n",left,"\n",right)
    # print(down)

if __name__ == "__main__":
  main()

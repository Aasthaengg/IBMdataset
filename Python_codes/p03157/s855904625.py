import queue
def main():
    h, w = map(int, input().split())
    s = [input().rstrip() for _ in range(h)]
    g = [[0 for j in range(w)] for i in range(h)]
    num = 1
    q = queue.Queue()
    for i in range(h):
        for j in range(w):
            if g[i][j] != 0:
                continue
            q.put([i, j])
            g[i][j] = num
            while not q.empty():
                y, x = q.get()
                if 0 < y and g[y-1][x] == 0 and s[y][x] != s[y-1][x]:
                    g[y-1][x] = num
                    q.put([y-1, x])
                if y < h-1 and g[y+1][x] == 0 and s[y][x] != s[y+1][x]:
                    g[y+1][x] = num
                    q.put([y+1, x])
                if 0 < x and g[y][x-1] == 0 and s[y][x] != s[y][x-1]:
                    g[y][x-1] = num
                    q.put([y, x-1])
                if x < w-1 and g[y][x+1] == 0 and s[y][x] != s[y][x+1]:
                    g[y][x+1] = num
                    q.put([y, x+1])
            num += 1
    blk, wht = [0]*(num+1), [0]*(num+1)
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                blk[g[i][j]] += 1
            else:
                wht[g[i][j]] += 1
    ans = 0
    for i in range(num+1):
        ans += blk[i] * wht[i]
    print(ans)

if __name__ == "__main__":
    main()

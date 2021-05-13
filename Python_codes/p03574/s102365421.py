def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()
    
    h, w = map(int, input().split())
    g = [[] for _ in range(h)]
    di = [-1, 0, 1, 0, 1, 1, -1, -1]
    dj = [0, 1, 0, -1, 1, -1, -1, 1]

    for i in range(h):
        g[i] = list(input())
        
    for i in range(h):
        for j in range(w):
            if g[i][j] == '#':
                continue
            
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if ni < 0 or ni >= h or nj < 0 or nj >= w:
                    continue
                if g[ni][nj] == '#':
                    cnt += 1
            g[i][j] = str(cnt)
    
    for i in g:
        print(''.join(i))

            



if __name__ == '__main__':
    main()
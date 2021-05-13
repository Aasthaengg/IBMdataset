def main():
    h,w = map(int,input().split())
    s = [list(input()) for _ in range(h)]

    cnt = [[0]*w for _ in range(h)]
    for i in range(h):
        prev = [0]*w
        for j in range(w):
            if s[i][j] == '#':
                continue
            if prev[j] == 1:
                continue
            ln = 0
            while j+ln < w:
                if s[i][j+ln] == '#':
                    break
                ln += 1
            for k in range(ln):
                cnt[i][j+k] += ln
                prev[j+k] = 1
    for j in range(w):
        prev = [0]*h
        for i in range(h):
            if s[i][j] == '#':
                continue
            if prev[i] == 1:
                continue
            ln = 0
            while i+ln < h:
                if s[i+ln][j] == '#':
                    break
                ln += 1
            for k in range(ln):
                cnt[i+k][j] += ln
                prev[i+k] = 1
    res = 0
    for i in range(h):
        for j in range(w):
            res = max(res, cnt[i][j]-1)
    print(res)

if __name__ == '__main__':
    main()

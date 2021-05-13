def main():
    n = int(input())
    a = [None]*n
    for i in range(n):
        x, y = map(int, input().split())
        a[i] = [x, y]
    p, q = 0, 0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            sp, sq = a[i][0]-a[j][0], a[i][1]-a[j][1]
            scnt = 0
            for k in range(n):
                for l in range(n):
                    if k == l:
                        continue
                    if a[k][0]-a[l][0] == sp and a[k][1]-a[l][1] == sq:
                        scnt += 1
            if scnt > cnt:
                cnt = scnt
                p = sp
                q = sq
    print(n-cnt)

if __name__ == "__main__":
    main()
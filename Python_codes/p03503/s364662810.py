def main():
    n = int(input())
    f = [list(map(int,input().split())) for i in range(n)]
    p = [list(map(int,input().split())) for i in range(n)]
    bit = 1<<10
    res = -10**10
    for i in range(1,bit):
        chk = [0]*n
        cnt = 0
        for j in range(10):
            if (i>>j)&1:
                for k in range(n):
                    if f[k][j] == 1:
                        chk[k] += 1
        for l in range(n):
            cnt += p[l][chk[l]]
        res = max(res,cnt)
    print(res)

if __name__ == '__main__':
    main()


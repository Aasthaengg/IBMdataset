def main():
    import itertools
    n,m = map(int,input().split())
    lt = []
    for i in range(m):
        lt.append(list(map(int,input().split())))
    p = list(map(int,input().split()))
    stats = ((0,1) for i in range(n))
    ans = 0
    for stat in itertools.product(*stats):
        flg = 0
        for i in range(m):
            cnt = 0
            for j in range(1,lt[i][0]+1):
                if stat[lt[i][j]-1]==1:
                    cnt+=1
            if cnt%2!=p[i]:
                flg = 1
                break
        if flg==0:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()

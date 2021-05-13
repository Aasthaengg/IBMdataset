def main():
    import bisect
    n,m = map(int,input().split())
    d = [[] for i in range(n)]
    ans = [0 for i in range(m)]
    for i in range(m):
        p,y = map(int,input().split())
        d[p-1].append((y,i))
    for i,d_ in enumerate(d):
        d_.sort()
        for c, d__ in enumerate(d_):
            ans[d__[1]] = str(i+1).zfill(6) + str(c+1).zfill(6)
    for i in range(m):
        print(ans[i])

if __name__ == "__main__":
    main()

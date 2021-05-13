def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, m = map(int, input().split())
    S = []
    for i in range(m):
        k, *s = map(int, input().split())
        s = [i-1 for i in s]
        S.append(s)
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**n):
        check = [False]*m
        for j in range(m):
            s = S[j]
            cnt = 0
            for idx in s:
                if (i>>idx)&1:
                    cnt += 1
            if cnt%2 == p[j]:
                check[j] = True
        if not False in check:
            ans += 1
    print(ans)

        

if __name__ == '__main__':
    main()
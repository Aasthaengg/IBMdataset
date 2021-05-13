def main():
    n = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))[::-1]
    mod = 1000000007
    if n == 1:
        if T[0] == A[0]:
            print(1)
        else:
            print(0)
        exit()
    INF = 1e+10
    ans = [[0, INF] for _ in range(n)]
    ans[0] = [1, T[0]]
    ans[-1] = [1, A[0]]
    for i, (t, a) in enumerate(zip(T[1:], A[1:])):
        i += 1
        an = ans[i]
        if t > T[i - 1]:
            if (an[0] == 0 and an[1] >= t) or (an[0] == 1 and an[1] == t):
                ans[i] = [1, t]
            else:
                print(0)
                exit()
        else:
            if an[0] == 0:
                ans[i][1] = min(ans[i][1], t)
            else:
                if an[1] > t:
                    print(0)
                    exit()
                else:
                    pass
        an = ans[-(i + 1)]
        if a > A[i - 1]:
            if (an[0] == 0 and an[1] >= a) or (an[0] == 1 and an[1] == a):
                ans[-(i + 1)] = [1, a]
            else:
                print(0)
                exit()
        else:
            if an[0] == 0:
                ans[-(i + 1)][1] = min(ans[-(i + 1)][1], a)
            else:
                if an[1] > a:
                    print(0)
                    exit()
                else:
                    pass
    c = 1
    for a in ans:
        if a[0] == 0:
            c = c * a[1] % mod
    print(c)

if __name__ == '__main__':
    main()

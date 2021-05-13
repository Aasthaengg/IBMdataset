from bisect import bisect_left
def main():
    A, B, q = map(int, input().split())
    INF = 10**18
    s = [-INF] + [int(input()) for _ in range(A)] + [INF]
    t = [-INF] + [int(input()) for _ in range(B)] + [INF]
    for _ in range(q):
        x = int(input())
        sind = bisect_left(s, x)
        tind = bisect_left(t, x)
        
        res = INF
        for S in [s[sind-1], s[sind]]:
            for T in [t[tind-1], t[tind]]:
                d1 = abs(x-S) + abs(S-T)
                d2 = abs(x-T) + abs(T-S)
                res = min([res, d1, d2])
        print(res)
main()
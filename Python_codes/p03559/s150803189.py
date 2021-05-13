def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    A.sort()
    B.sort()
    C.sort()
    Bdic = [0]*N
    from bisect import bisect
    from itertools import accumulate
    for i, b in enumerate(B):
        idx = bisect(C, b)
        Bdic[i] = N - idx
    Bacc = list(accumulate([b for b in Bdic + [0]][::-1]))[::-1]
    ans = 0
    for i, a in enumerate(A):
        idx = bisect(B, a)
        ans += (Bacc[idx])
    print(ans)


if __name__ == '__main__':
    main()

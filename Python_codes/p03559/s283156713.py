import bisect

def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    C = sorted(list(map(int, input().split())))
    ans = 0
    for b in B:
        indexa = bisect.bisect_left(A, b)
        indexc = bisect.bisect_right(C, b)
        ans += indexa * (N - indexc)
    print(ans)

if __name__ == '__main__':
    main()

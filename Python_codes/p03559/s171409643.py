def main():
    N = int(input())
    *a, = map(int, input().split())
    *b, = map(int, input().split())
    *c, = map(int, input().split())

    a.sort()
    b.sort()
    c.sort()

    ans = 0
    ai = 0  # [0,ai)
    ci = 0  # [ci,N)
    for mid in b:
        while ai < N and a[ai] < mid:
            ai += 1

        while ci < N and c[ci] <= mid:
            ci += 1

        ans += ai * (N - ci)

    print(ans)


if __name__ == '__main__':
    main()

# import sys
# input = sys.stdin.readline
# 
# sys.setrecursionlimit(10 ** 7)
# 
# (int(x)-1 for x in input().split())
# rstrip()

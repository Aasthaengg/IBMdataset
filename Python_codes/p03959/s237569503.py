# code-festival-2016-qualcC - 二人のアルピニスト / Two Alpinists
from bisect import bisect_left as bs


def main():
    """
      /----\     <- xi (= yi)
     /      \--\
    /           \
      xi  yi
    0 ~ xi / xi ~ yi / yi+1 ~ N-1
    """
    N = int(input())
    T = tuple(map(int, input().split()))
    A = tuple(map(int, input().split()))
    x, y = T[-1], A[0]  # max of x, y
    xi, yi = T.index(x), N - A[::-1].index(y) - 1  # indices of x, y
    if x != y or xi > yi:
        print(0)
        return
    MOD = 10 ** 9 + 7
    ans, cur = 1, 0
    for i in T[: xi + 1]:
        if i > cur:  # point of new altitude -> no choice (ans * 1)
            cur = i
        else:
            ans = (ans * cur) % MOD  # mulitple choices (1, 2, ..., cur)
    for _ in range(xi + 1, yi):
        ans = (ans * cur) % MOD
    for i in A[yi + 1 :]:
        if i < cur:
            cur = i
        else:
            ans = (ans * cur) % MOD
    print(ans)


if __name__ == "__main__":
    main()
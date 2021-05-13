from bisect import bisect_right

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a = sorted(a)
    b = sorted(b)
    c = sorted(c)

    ans = 0

    # まずあるbを選んだ時のcの組み合わせの数のリストを作る。
    clist = [0] * n
    clist[n-1] = n - bisect_right(c, b[n-1])
    for i in range(n-2, -1, -1):
        clist[i] = n - bisect_right(c, b[i]) + clist[i+1]

    for aa in a:
        b_pos = bisect_right(b, aa)
        if b_pos != n:
            ans += clist[b_pos]

    print(ans)

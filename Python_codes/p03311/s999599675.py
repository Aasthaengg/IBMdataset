def main():
    N = int(input())
    A = [x - i for i, x in enumerate(map(int, input().split()), start=1)]
    A.sort()

    m = A[N // 2]  # 個数の偶奇によらず、この点は絶対値の総和を最小にする

    ans = sum(abs(x - m) for x in A)

    print(ans)


if __name__ == '__main__':
    main()

def main():
    N = int(input())  # 文字列または整数(一変数)

    mins = []
    maxs = []

    for i in range(N):
        a, b = map(int, input().split())
        mins.append(a)
        maxs.append(b)

    mins.sort()
    maxs.sort()

    if N % 2 == 1:
        # 奇数の場合
        mid = N // 2
        print(maxs[mid] - mins[mid] + 1)

    else:
        mid1 = N // 2
        mid2 = mid1 - 1
        smallest = mins[mid1] + mins[mid2]
        largest = maxs[mid1] + maxs[mid2]
        print(largest - smallest + 1)


if __name__ == '__main__':
    main()

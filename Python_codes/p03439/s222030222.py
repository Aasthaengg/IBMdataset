import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def query(n: int):
    print(n, flush=True)
    res = input().rstrip()[0]
    if res == "V":
        sys.exit()
    return res


def main():
    n = input_int()
    record = [None] * n
    # 方針：
    # 2分探索で探す
    # 初期状態を見つける
    left = 0
    right = n - 1
    record[left] = query(left)
    record[right] = query(right)

    for i in range(18):
        mid = (left + right) // 2
        record[mid] = query(mid)
        if (mid - left) % 2 == 1:
            # 差が奇数で性別が一致する場合は空白が間に存在する
            if record[left] == record[mid]:
                right = mid
            else:
                left = mid
        else:
            # 差が偶数で性別が一致する場合は空白が間に存在しない
            if record[left] == record[mid]:
                left = mid
            else:
                right = mid

    return


if __name__ == "__main__":
    main()

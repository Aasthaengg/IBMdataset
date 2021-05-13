import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    h, w = input_int_list()
    ans = []
    grid = []
    for _ in range(h):
        grid.append(input_int_list())
    # 行ごとに左から偶数を作っていく
    # 右端での調整は1行したに渡す
    # 計算量: O(hw)

    for i in range(h):
        for j in range(w):
            if grid[i][j] % 2 == 1:
                if i == h - 1 and j == w - 1:
                    break
                grid[i][j] -= 1
                if j < w - 1:
                    grid[i][j + 1] += 1
                    ans.append((i + 1, j + 1, i + 1, j + 2))  # 1-indexed
                elif i < h - 1:
                    grid[i + 1][j] += 1
                    ans.append((i + 1, j + 1, i + 2, j + 1))  # 1-indexed

    print(len(ans))
    for query in ans:
        print(*query)

    return


if __name__ == "__main__":
    main()

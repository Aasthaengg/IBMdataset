def main():
    width = int(input())
    grid = [input() for _ in range(2)]
    mod = 1000000007
    index = 0
    answer = 0
    former_grid = 0  # 1:上下同じ，0:上下が異なる
    while index < width:
        if index == 0:
            if grid[0][index] == grid[1][index]:
                answer = 3
                former_grid = 1
            else:
                answer = 6
                former_grid = 0
                index += 1
        else:
            if former_grid:
                # 直前が縦方向に置いていたとき
                answer = answer * 2 % mod
                if not grid[0][index] == grid[1][index]:
                    index += 1
                    former_grid = 0
            else:
                # 直前が横方向に置いていたとき
                if grid[0][index] == grid[1][index]:
                    former_grid = 1
                else:
                    answer = answer * 3 % mod
                    index += 1
        index += 1
    print(answer)


if __name__ == '__main__':
    main()


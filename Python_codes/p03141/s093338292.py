def main():
    N = int(input())
    input_list = [list(map(int, input().split())) for _ in range(N)]
    dish_list = [(sum(row), row[0], row[1], n) for n, row in enumerate(input_list)]
    dish_list.sort(reverse=True)
    ans = sum([((- 1)**(n % 2)) * dish[1 + n % 2] for n, dish in enumerate(dish_list)])
    print(ans)


if __name__ == '__main__':
    main()
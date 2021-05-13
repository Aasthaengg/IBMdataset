def main():
    n, m = map(int, input().split())
    food_list = [0] * m

    for _ in range(n):
        a_list = list(map(int, input().split()))
        for i in range(1, a_list[0] + 1):
            food_list[a_list[i] - 1] += 1

    cnt = 0
    for food in food_list:
        if food == n:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()

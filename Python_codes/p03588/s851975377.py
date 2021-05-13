def main():
    N = int(input())  # 文字列または整数(一変数)


    max_a = 0
    min_b = None

    for i in range(N):
        a, b = map(int, input().split())
        if a > max_a:
            max_a = a
            min_b = b

    answer = max_a + min_b
    print(answer)


if __name__ == '__main__':
    main()

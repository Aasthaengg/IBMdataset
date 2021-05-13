def main():
    n = int(input())
    d, x = map(int, input().split())
    num_list = [int(input()) for _ in range(n)]

    count = 0
    for num in num_list:
        if d // num > 0 and d % num == 0:
            count += d // num
        elif d //num >0:
            count += d // num + 1
        else:
            count += 1

    ans = count + x

    print(ans)


if __name__ == '__main__':
    main()

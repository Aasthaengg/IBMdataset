def divide_by_two(a):
    cnt = 0
    while True:
        if a % 2 == 0:
            a //= 2
            cnt += 1
        else:
            break

    return cnt


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    ans = 10 ** 9

    for a in a_list:
        ans = min(ans, divide_by_two(a))

    print(ans)


if __name__ == "__main__":
    main()

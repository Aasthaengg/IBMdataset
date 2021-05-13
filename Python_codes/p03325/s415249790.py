def divide_by_2(n):
    cnt = 0
    while True:
        if n % 2 == 0:
            n //= 2
            cnt += 1
        else:
            break
    return cnt


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    ans = 0

    for a in a_list:
        ans += divide_by_2(a)

    print(ans)


if __name__ == "__main__":
    main()

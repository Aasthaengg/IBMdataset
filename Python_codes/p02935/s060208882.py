def main():
    n = int(input())
    v_list = list(map(int, input().split()))
    v_list.sort()
    ans = 0

    for i in range(n):
        if i == 0 or i == 1:
            ans += v_list[i] / 2 ** (n - 1)
        else:
            ans += v_list[i] / 2 ** (n - i)

    print(ans)


if __name__ == "__main__":
    main()

def main():
    n, t = map(int, input().split())
    t_list = list(map(int, input().split()))
    ans = 0

    for i in range(n - 1):
        if t_list[i] + t < t_list[i + 1]:
            ans += t
        else:
            ans += t_list[i + 1] - t_list[i]

    print(ans + t)


if __name__ == "__main__":
    main()

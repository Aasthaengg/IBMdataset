def main():
    N = int(input())
    t_lst = [0] * (N + 1)
    x_lst = [0] * (N + 1)
    y_lst = [0] * (N + 1)

    for i in range(1, N + 1):
        t, x, y = map(int, input().split())
        t_lst[i] = t
        x_lst[i] = x
        y_lst[i] = y

    ans = "Yes"
    for i in range(N):
        dt = t_lst[i + 1] - t_lst[i]
        dist = abs(x_lst[i + 1] - x_lst[i]) + abs(y_lst[i + 1] - y_lst[i])
        if dt < dist:
            ans = "No"
            break
        elif dt % 2 != dist % 2:
            ans = "No"
            break

    print(ans)


if __name__ == "__main__":
    main()

def main():
    path_list = [0] * 4

    for _ in range(3):
        a, b = map(int, input().split())
        path_list[a - 1] += 1
        path_list[b - 1] += 1

    odd, even = 0, 0
    for path in path_list:
        if path % 2 == 0:
            even += 1
        else:
            odd += 1

    if even == 4 or odd == 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()

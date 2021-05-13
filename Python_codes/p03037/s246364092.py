def main():
    x = list(map(int, input().split()))
    n = x[0]
    m = x[1]

    common_section = [1, n]

    for i in range(m):
        a = list(map(int, input().split()))
        if a[0] > common_section[0]:
            common_section[0] = a[0]
        if a[1] < common_section[1]:
            common_section[1] = a[1]

    answer = common_section[1] - common_section[0] + 1
    if answer < 0:
        answer = 0
    print(answer)


if __name__ == "__main__":
    main()

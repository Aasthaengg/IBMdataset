def main():
    L, R = map(int, input().split())
    if R - L + 1 >= 2019:
        print(0)
        exit()
    vals = []
    for i in range(L, R):
        for j in range(i+1, R+1):
            vals.append(((i % 2019) * (j % 2019)) % 2019)
    print(min(vals))


if __name__ == '__main__':
    main()

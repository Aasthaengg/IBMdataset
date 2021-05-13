def main():
    N = int(input())
    data = [input().split() for _ in range(N)]
    sum = 0
    for d in data:
        if d[1] == "JPY":
            sum += int(d[0])
        else:
            sum += float(d[0]) * 380000
    print(sum)


if __name__ == '__main__':
    main()

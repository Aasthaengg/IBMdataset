def main():
    n, a, b = map(int, input().split(" "))
    x = list(map(int, input().split(" ")))
    fatigue = 0
    current = x[0]

    for x_i in x[1:]:
        fatigue = fatigue + min((x_i - current) * a, b)
        current = x_i
    print(fatigue)


if __name__ == '__main__':
    main()
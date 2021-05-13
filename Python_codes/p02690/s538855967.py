def main():
    x = int(input())
    gojo = [int(i**5) for i in range(-1100, 1100)]
    for i, v1 in enumerate(gojo):
        x1 = i - 1100
        for j, v2 in enumerate(gojo):
            x2 = j - 1100
            if v1 - v2 == x:
                print(x1, x2)
                return


if __name__ == '__main__':
    main()

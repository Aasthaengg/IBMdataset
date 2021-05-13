def main():
    n = int(input())
    s = input()
    x = 0
    max_s = 0

    for i in range(n):
        if s[i] == 'I':
            x += 1
        elif s[i] == 'D':
            x -= 1

        if max_s < x:
            max_s = x

    print(max_s)


if __name__ == "__main__":
    main()

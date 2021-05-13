def main():
    a, b, c, d = map(int, input().split())
    x = [a, b]
    y = [c, d]
    z = []
    for i in x:
        for k in y:
            z.append(i * k)
    print(max(z))


if __name__ == '__main__':
    main()

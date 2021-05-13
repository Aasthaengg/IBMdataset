def main():
    n, d = map(int, input().split())
    x = 1

    while True:
        monitoring = (2*d+1) * x

        if monitoring < n:
            x += 1
        else:
            break

    print(x)

if __name__ == '__main__':
    main()
def main():
    a, b, c = (int(i) for i in input().split())
    for k in range(c):
        if k % 2 == 0:
            b += a//2
            a //= 2
        else:
            a += b//2
            b //= 2
    print(a, b)


if __name__ == '__main__':
    main()

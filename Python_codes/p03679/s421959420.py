def main():
    x, a, b = (int(i) for i in input().split())
    day = -a+b
    if day <= 0:
        print("delicious")
    elif day <= x:
        print("safe")
    else:
        print("dangerous")


if __name__ == '__main__':
    main()

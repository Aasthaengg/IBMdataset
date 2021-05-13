def main():
    x, y = (int(x) for x in input().split())
    prod = x*y
    if (prod % 2):
        print("Odd", sep="")
    else:
        print("Even", sep="")


if __name__ == '__main__':
    main()

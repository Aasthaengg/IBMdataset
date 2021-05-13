def main():
    s = list(input())
    start, end = s[0], s[-1]
    midle = len(s[1:-1])
    print("{}{}{}".format(start, midle, end))


if __name__ == "__main__":
    main()

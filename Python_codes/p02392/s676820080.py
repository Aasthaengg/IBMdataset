def main():
    a,b,c = map(int, input().split())
    f = 1
    if a > b or a == b:
        f = 0
    else:
        if b > c or b == c:
            f = 0

    if f == 0:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
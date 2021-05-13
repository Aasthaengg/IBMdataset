def main():
    n = input().split()
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])

    if a < b < c:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
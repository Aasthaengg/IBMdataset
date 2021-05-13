def main():
    a, b, c = (int(i) for i in input().split())
    if b - a == c - b:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()

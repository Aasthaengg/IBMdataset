def main():
    a, b = map(int, input().split())
    diff = b - a
    height = 0
    for i in range(1, diff+1):
        height += i
    ans = height - b
    print(ans)


if __name__ == "__main__":
    main()

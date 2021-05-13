def main():
    x, a, b = map(int, input().split())
    if abs(x-a) < abs(x-b):
        ans = 'A'
    else:
        ans = 'B'
    print(ans)


if __name__ == "__main__":
    main()

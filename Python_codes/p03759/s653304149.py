def main():
    a, b, c = map(int, input().split())
    if b - a == c - b:
        ans = 'YES'
    else:
        ans = 'NO'
    print(ans)


if __name__ == "__main__":
    main()

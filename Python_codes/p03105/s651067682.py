def main():
    a, b, c = map(int, input().split())
    cnt = 0
    current = a
    while current <= b:
        if cnt == c:
            break
        cnt += 1
        current += a
    print(cnt)


if __name__ == "__main__":
    main()

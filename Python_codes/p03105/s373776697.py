def main():
    a, b, c = map(int, input().split())
    Count = 0
    while True:
        b = b-a
        if Count == c or b < 0:
            break
        Count += 1
    print(Count)


if __name__ == "__main__":
    main()

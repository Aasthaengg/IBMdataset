def main():
    w, a, b = map(int, input().split())

    if a <= b <= a + w or a <= b + w <= a + w:
        print(0)
    elif b <= a <= b + w or b <= a + w <= b + w:
        print(0)
    else:
        print(min(abs(a + w - b), abs(b + w - a)))


if __name__ == "__main__":
    main()

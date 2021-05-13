def main():
    width, a, b = map(int, input().split())
    print(0 if a <= b <= a + width else min(abs(b - a - width), abs(a - b - width)))


if __name__ == '__main__':
    main()


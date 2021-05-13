def main():
    h1, m1, h2, m2, k = map(int, input().split())
    x = 60 * h1 + m1
    y = 60 * h2 + m2 - k
    print(max(0, y - x))

if __name__ == '__main__':
    main()

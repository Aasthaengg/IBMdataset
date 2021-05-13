def main():
    n = int(input())
    x = 0
    y = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if x < a:
            x = a
            y = b
    print(x + y)

if __name__ == "__main__":
    main()

def main():
    n, a, b = map(int, input().split())

    if (b - a) % 2 == 0:
        ans = (b - a) // 2
    else:
        ans = min(n - b, a - 1) + 1 + (b - a - 1) // 2
    
    print(ans)


if __name__ == "__main__":
    main()

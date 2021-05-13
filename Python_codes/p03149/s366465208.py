def main():
    numbers = sorted(list(map(int, input().split())))
    print("YES" if numbers == [1, 4, 7, 9] else "NO")


if __name__ == '__main__':
    main()


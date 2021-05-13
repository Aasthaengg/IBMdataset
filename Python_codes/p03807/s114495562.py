def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    count_odd = 0
    for num in numbers:
        if num % 2:
            count_odd += 1
    print("YES" if count_odd % 2 == 0 else "NO")


if __name__ == '__main__':
    main()


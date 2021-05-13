def main():
    n = int(input())
    i = 1
    answer = 0
    while i * i <= n:
        if (n - i) % i == 0 and n - i > i ** 2:
            answer += (n - i) // i
        i += 1
    print(answer)


if __name__ == '__main__':
    main()


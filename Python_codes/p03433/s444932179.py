
def main():
    n = int(input())
    a = int(input())
    if a - (n - (500 * (n // 500))) >= 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()

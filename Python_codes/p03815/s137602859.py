def main():
    x = int(input())
    ans, r = divmod(x, 11)
    if r == 0:
        print(2 * ans)
    elif 1 <= r <= 6:
        print(2 * ans + 1)
    else:
        print(2 * ans + 2)

if __name__ == '__main__':
    main()

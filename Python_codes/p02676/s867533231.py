def main() -> None:
    k = int(input())
    s = input()

    print(s if len(s) <= k else s[:k]+'...')

    return


if __name__ == '__main__':
    main()

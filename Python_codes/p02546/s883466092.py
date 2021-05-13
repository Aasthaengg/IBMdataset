def main() -> None:
    s = input()

    print(s + 's' if s[-1] != 's' else s + 'es')

    return


if __name__ == '__main__':
    main()

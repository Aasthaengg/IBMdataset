def answer(s: str) -> str:
    return s[::2]


def main():
    s = input()
    print(answer(s))


if __name__ == '__main__':
    main()
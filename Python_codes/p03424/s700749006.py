def answer(n: str, s: str) -> str:
    return 'Three' if len(set(s.split())) == 3 else 'Four'


def main():
    n = input()
    s = input()
    print(answer(n, s))


if __name__ == '__main__':
    main()
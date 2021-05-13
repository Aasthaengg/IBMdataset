def answer(s: str) -> int:
    return s.rfind('Z') - s.find('A') + 1


def main():
    s = input()
    print(answer(s))


if __name__ == '__main__':
    main()

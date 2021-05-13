def answer(n: int, l: []) -> str:
    return 'Yes' if l.pop(l.index(max(l))) < sum(l) else 'No'


def main():
    n = int(input())
    l = list(map(int, input().split()))
    print(answer(n, l))


if __name__ == '__main__':
    main()
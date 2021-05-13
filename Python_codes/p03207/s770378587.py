def answer(n: int, p: []) -> int:
    p.append(p.pop(p.index(max(p))) // 2)
    return sum(p)


def main():
    n = int(input())
    p = list(int(input()) for _ in range(n))
    print(answer(n, p))


if __name__ == '__main__':
    main()
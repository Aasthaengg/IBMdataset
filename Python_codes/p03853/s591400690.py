from typing import List


def answer(h: int, w: int, c: List[str]) -> str:
    result = ''
    for i in c:
        for j in range(2):
            result += f'{i}\n'

    return result[:-1]


def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    print(answer(h, w, c))


if __name__ == '__main__':
    main()

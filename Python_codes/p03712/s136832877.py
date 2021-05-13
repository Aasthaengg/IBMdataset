from typing import List


def answer(h: int, w: int, a: List[str]) -> List[str]:
    top_bottom_line = '#' * (w + 2)

    result = [top_bottom_line]
    for line in a:
        result.append(f'#{line}#')
    result.append(top_bottom_line)

    return result


def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    for i in answer(h, w, a):
        print(i)


if __name__ == '__main__':
    main()

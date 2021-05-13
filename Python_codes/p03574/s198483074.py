from typing import List


def search_bomb(i: int, j: int, ss: List[str]) -> int:
    count = 0
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if 0 <= k <= h - 1 and 0 <= l <= w - 1:
                if ss[k][l] == '#':
                    count += 1
    return count


def answer(ss: List[str]) -> List[str]:
    result = list('' for _ in range(h))

    for i, s in enumerate(ss):
        line = ''
        for j, c in enumerate(s):
            if c == '.':
                line += str(search_bomb(i, j, ss))
            elif c == '#':
                line += '#'
        result[i] = line

    return result


def main():
    ss = [input() for _ in range(h)]
    for line in answer(ss):
        print(line)


if __name__ == '__main__':
    h, w = map(int, input().split())
    main()

import sys
import re


def resolve(in_):
    N = int(next(in_))
    S = next(in_).strip()

    answer = sum(1 for _ in re.finditer('ABC', S))
    return answer


def main():
    answer = resolve(sys.stdin)
    print(answer)


if __name__ == '__main__':
    main()

from collections import defaultdict


def main():
    N, M = map(int, input().split())
    counter = defaultdict(int)
    for _ in range(M):
        A, B = map(lambda x: int(x) - 1, input().split())
        counter[A] += 1
        counter[B] += 1
    is_valid = True
    for v in counter.values():
        if v % 2 == 1:
            is_valid = False
            break
    if is_valid:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()

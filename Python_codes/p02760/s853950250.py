import sys
import itertools

def resolve(in_):
    A = tuple(map(int, itertools.chain.from_iterable(line.split() for line in itertools.islice(in_, 3))))
    assert len(A) == 9
    C = [False] * 9
    N = int(next(in_))
    # B = tuple(map(int, itertools.islice(in_, N)))
    B = frozenset(map(int, itertools.islice(in_, N)))

    for i, a in enumerate(A):
        if a in B:
            C[i] = True
    # print(f'{A=} {C=}')

    b = any(all(line) for line in itertools.chain(
        ((C[i * 3], C[i * 3 + 1], C[i * 3 + 2]) for i in range(3)),
        ((C[i], C[i + 3], C[i + 6]) for i in range(3)),
        ((C[0], C[4], C[8]), (C[2], C[4], C[6])),
    ))
    return 'Yes' if b else 'No'


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()

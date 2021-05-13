import sys
import itertools

def is_prime(x):
    if x == 2:
        return True

    pred = lambda v: v * v <= x
    it = itertools.chain((2,), itertools.count(3, 2))
    return not any(not (x % i) for i in itertools.takewhile(pred, it))
        

def resolve(in_):
    X = int(next(in_))
    for i in itertools.count(X):
        if is_prime(i):
            return i


def main():
    answer = resolve(sys.stdin)
    print(answer)


if __name__ == '__main__':
    main()

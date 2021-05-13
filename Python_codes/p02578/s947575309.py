import sys


def resolve(in_):
    N = int(next(in_))
    A = tuple(map(int, next(in_).split()))

    stool = 0
    height = A[0]
    for h in A[1:]:
        if height <= h:
            height = h
        else:
            stool += height - h

    return stool

def main():
    answer = resolve(sys.stdin)
    print(answer)


if __name__ == '__main__':
    main()

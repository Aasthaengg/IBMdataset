import sys
import itertools


def resolve(in_):
    N = int(next(in_))
    AB = (map(int, line.split()) for line in itertools.islice(in_, N))
    A = []
    B = []
    for a, b in AB:
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()


    i = N // 2
    if N % 2:
        a_median = A[i]
        b_median = B[i]
        if a_median > b_median:
            a_median, b_median = b_median, a_median
        answer = len(range(a_median, b_median + 1))
    else:
        a_median2 = (A[i - 1] + A[i])  #  / 2
        b_median2 = (B[i - 1] + B[i])  # / 2
        if a_median2 > b_median2:
            a_median2, b_median2 = b_median2, a_median2
        answer = len(range(a_median2, b_median2 + 1))
            
    return answer


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()

from sys import stdin


def find_sum_of_digits(n, base=10):
    _sum = 0
    while n>0:
        _sum += n%base
        n //= base
    return _sum


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N = int(_in[0])  # type:int
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    cnt = float('inf')
    for A in range(1,N):
        B = N-A
        sum_ = find_sum_of_digits(A)+find_sum_of_digits(B)
        cnt = min(cnt,sum_)
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)

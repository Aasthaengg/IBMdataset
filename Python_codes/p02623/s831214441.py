#
#   max I + J
#     with
#       \sum_{i <= I} Ai + \sum_{j <= J} Bi <= K
#
def solve(ls1, ls2, k):
    n, m = len(ls1), len(ls2)

    # Make cumsum
    for i in range(n - 1):
        ls1[i + 1] += ls1[i]

    for i in range(m - 1):
        ls2[i + 1] += ls2[i]
    ls1 = [0] + ls1
    ls2 = [0] + ls2

    # Find maximum by
    #   1. Initially (I, J) = (0, maxJ)
    #   2. Increase I and decrease J

    # Initialize
    for j in range(m + 1)[::-1]:
        if ls2[j] <= k:
            J = j
            break
    ij_max = J

    # Increase/decrease
    I = 0
    while I <= n and J >= 0:
        while I <= n and ls1[I] + ls2[J] <= k:
            I += 1
        ij_max = max(ij_max, I + J - 1)
        J -= 1

    return ij_max


def main(istr, ostr):
    n, m, k = list(map(int, istr.readline().strip().split()))
    ls1 = list(map(int, istr.readline().strip().split()))
    ls2 = list(map(int, istr.readline().strip().split()))
    result = solve(ls1, ls2, k)
    print(result, file=ostr)


if __name__ == "__main__":
    import sys

    main(sys.stdin, sys.stdout)

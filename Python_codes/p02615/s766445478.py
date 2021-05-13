def solve(ls, debug=0):
    n = len(ls)
    ls = sorted(ls)
    result = 0
    # Pick once largest
    if n >= 2:
        result += ls[-1]
    # Pick twice for each next larger one
    for i in range(2, n):
        result += ls[-1 - i // 2]
    return result


def main(istr, ostr):
    n = int(istr.readline())
    ls = list(map(int, istr.readline().strip().split()))
    print(solve(ls), file=ostr)


if __name__ == "__main__":
    import sys

    main(sys.stdin, sys.stdout)

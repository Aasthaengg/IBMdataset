def main(istr, ostr):
    n, k = list(map(int, istr.readline().strip().split()))
    ls = list(map(int, istr.readline().strip().split()))
    ls.sort()
    result = sum(ls[:k])
    print(result, file=ostr)


if __name__ == "__main__":
    import sys

    main(sys.stdin, sys.stdout)


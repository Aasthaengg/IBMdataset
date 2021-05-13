def main(istr, ostr):
    ls = list(map(int, istr.readline().strip().split()))
    for i in range(5):
        if ls[i] == 0:
            print(i + 1, file=ostr)


if __name__ == "__main__":
    import sys

    main(sys.stdin, sys.stdout)

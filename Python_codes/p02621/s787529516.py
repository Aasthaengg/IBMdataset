def main(istr, ostr):
    a = int(istr.readline())
    print(a + a * (a + a * a), file=ostr)


if __name__ == "__main__":
    import sys

    main(sys.stdin, sys.stdout)

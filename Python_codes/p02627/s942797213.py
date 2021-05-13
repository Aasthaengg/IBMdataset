def main(istr, ostr):
    s = istr.readline().strip()
    if 'a' <= s and s <= 'z':
        print('a', file=ostr)
    else:
        print('A', file=ostr)


if __name__ == "__main__":
    import sys

    main(sys.stdin, sys.stdout)

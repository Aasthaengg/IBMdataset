#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(r: int, g: int, b: int):
    return YES if int(str(''.join(map(str, [r, g, b])))) % 4 == 0 else NO


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    r = int(next(tokens))  # type: int
    g = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    print(solve(r, g, b))

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()

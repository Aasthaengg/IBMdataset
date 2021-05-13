import sys
import functools
import collections
import operator


def resolve(in_):
    n = int(next(in_))
    s = next(in_).strip()

    c = collections.Counter()
    c[b'R'[0]] = 0
    c[b'G'[0]] = 0
    c[b'B'[0]] = 0
    c.update(s)
    ans = functools.reduce(operator.mul, c.values())
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            k = j * 2 - i
            if k - 1 >= n:
                break
            si = s[i - 1]
            sj = s[j - 1]
            sk = s[k - 1]
            if si != sj and sj != sk and sk != si:
                ans -= 1
    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
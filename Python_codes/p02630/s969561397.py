def solve(ls1, ls2):
    s = sum(ls1)
    m = {}
    for a in ls1:
        if not a in m:
            m[a] = 0
        m[a] += 1

    result = []
    for b, c in ls2:
        if not b in m:
            result.append(s)
            continue
        if not c in m:
            m[c] = 0
        s += (c - b) * m[b]
        m[c] += m[b]
        m[b] = 0
        result.append(s)
    return result


def main(istr, ostr):
    (n,) = list(map(int, istr.readline().strip().split()))
    ls1 = list(map(int, istr.readline().strip().split()))
    (q,) = list(map(int, istr.readline().strip().split()))
    ls2 = [0] * q
    for i in range(q):
        ls2[i] = list(map(int, istr.readline().strip().split()))
    result = solve(ls1, ls2)
    print(*result, sep="\n", file=ostr)


if __name__ == "__main__":
    import sys

    main(sys.stdin, sys.stdout)

import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    XL = []
    for i in range(N):
        x, l = map(int, input().strip().split())
        XL.append((x, l))
    return N, XL


def solve(N, XL):
    XL.sort(key=lambda x: x[0]+x[1])
    r = -10**9-1
    count = 0
    for x, l in XL:
        if r <= x - l:
            r = x + l
            count += 1
    return count


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))

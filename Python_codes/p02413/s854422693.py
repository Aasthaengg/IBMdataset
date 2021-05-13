# coding=utf-8


def main():
    r, c = map(int, raw_input().split())
    rSum = [0] * (c + 1)
    for _ in xrange(r):
        row = map(int, raw_input().split() + ['0'])
        row[-1] = sum(row)
        print ' '.join(map(str, row))
        for i in xrange(c + 1):
            rSum[i] += row[i]
    print ' '.join(map(str, rSum))

if __name__ == '__main__':
    main()
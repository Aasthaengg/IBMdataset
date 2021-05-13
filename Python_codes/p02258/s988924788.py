import sys

def solve():
    n = int(raw_input())
    R = []

    for i in xrange(n):
        R.append(int(raw_input()))

    #for i in xrange(n):
    #    print R[i]

    max_profit = -sys.maxint
    min_R = R[0]

    for i in xrange(1, n):
        if R[i] - min_R > max_profit:
            max_profit = R[i] - min_R
        if min_R > R[i]:
            min_R = R[i]

    print max_profit


if __name__ == "__main__":
    solve()
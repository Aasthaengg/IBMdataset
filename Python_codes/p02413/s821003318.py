if __name__ == "__main__":

    n, m = map(int, raw_input().split())

    s = [0] * n * m

    for c in xrange(n):
        s[c*m:c*m+m] = map( int, raw_input().split())

    csum = [0] * n
    rsum = [0] * m
    for c in xrange(n):
        for r in xrange(m):
            csum[c] += s[m*c + r]
            rsum[r] += s[m*c + r]
            print s[m*c + r],
        print csum[c]
    asum = 0
    for i in xrange(m):
        asum += rsum[i]
        print rsum[i],
    print asum
def resolve():
    cands = [111,222,333,444,555,666,777,888,999]
    N = int(input())
    import bisect
    print(cands[bisect.bisect_left(cands, N)])

if '__main__' == __name__:
    resolve()
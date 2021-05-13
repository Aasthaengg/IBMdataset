def resolve():
    s = input()
    t = input()
    d = {}
    for i, c in enumerate(list(s)):
        d.setdefault(c, [])
        d[c].append(i)
    
    import bisect
    nloops = 0
    prev = -1
    for c in list(t):
        if c not in d:
            print(-1)
            return
        # prevより後ろにあるcのうち、最も近いものの位置
        cidx = bisect.bisect_left(d[c], prev)
        if cidx < len(d[c]) and prev == d[c][cidx]:
            cidx += 1
        nearc = d[c][cidx] if cidx < len(d[c]) else None
        if nearc is None:
            nloops += 1
            nearc = d[c][0]
        prev = nearc
    print(nloops*len(s)+prev+1)



if '__main__' == __name__:
    resolve()
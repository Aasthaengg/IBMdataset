def resolve():
    s = int(input())
    hist = set([])
    idx = 1
    while True:
        if s in hist:
            print(idx)
            return
        hist.add(s)
        idx += 1
        if s%2==0:
            s //= 2
        else:
            s = 3*s + 1



if '__main__' == __name__:
    resolve()
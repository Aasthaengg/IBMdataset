def resolve():
    A = int(input())
    B = int(input())
    cands = set([1,2,3])
    print(list(cands-set([A, B]))[0])

if '__main__' == __name__:
    resolve()
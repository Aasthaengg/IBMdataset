def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    absA = list(map(abs, A))
    negcnt = 0
    for a in A:
        if a < 0:
            negcnt += 1
    if 0 in A or negcnt%2==0:
        print(sum(absA))
    else:
        print(sum(absA)-2*min(absA))



if '__main__' == __name__:
    resolve()
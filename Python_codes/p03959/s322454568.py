
def main():
    n = int(input())
    t= list(map(int,input().split()))
    a= list(map(int,input().split()))


    maxh = t[:]
    minflag = [0 for _ in range(n)]

    if t[-1] != a[0]:
        return 0
    else:
        maxflag = t[-1]
    maxh[0] = t[0]
    minflag[0] = 1

    for i in range(1,n):
        if t[i] > t[i-1]:
            minflag[i] = 1

    maxh[-1] = a[-1]
    minflag[-1] = 1
    if a[-1] != t[-1]:
        for i in range(n-2,-1,-1):
            if a[i] > t[i]:
                return 0
            elif a[i] == t[i]:
                if a[i] != maxflag:
                    return 0
                else:
                    minflag[i] = 1
                    break
            maxh[i] = a[i]
            if a[i] > a[i+1]:
                minflag[i] = 1

    res = 1
    for i in range(n):
        if not minflag[i]:
            res *= maxh[i]
            res %= (10**9+7)
    return res % (10**9+7)

print(main())
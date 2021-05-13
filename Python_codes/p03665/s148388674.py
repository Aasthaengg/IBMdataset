import collections

def nCk(n, k):
    k = min(k, n-k)
    numer = 1
    for i in range(n, n-k, -1):
        numer *= i
    denom = 1
    for i in range(k, 1, -1):
        denom *= i
    return numer // denom

def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    B = [x%2 for x in A]
    Bcount = collections.Counter(B)
    if Bcount[1] == 0 and P == 1:
        print(0)
        return
    ans = 0
    if P == 0:
        tmp = pow(2, Bcount[0])
        for i in range(0, Bcount[1]+1, 2):
            ans += tmp * nCk(Bcount[1], i)
        print(ans)
        return
    else:
        tmp = pow(2, Bcount[0])
        for i in range(1, Bcount[1]+1, 2):
            ans += tmp * nCk(Bcount[1], i)
        print(ans)
    

if __name__ == "__main__":
    main()

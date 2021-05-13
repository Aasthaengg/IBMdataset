def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    L = [i+A[i-1] for i in range(1,N+1)]
    R = [i-A[i-1] for i in range(1,N+1)]
    import collections
    Lcnter = collections.Counter(L)
    Rcnter = collections.Counter(R)
    values = set(Lcnter.keys()) & set(Rcnter.keys())
    ans = 0
    for i in values:
        ans += Lcnter[i]*Rcnter[i]
    print(ans)
    


if __name__ == "__main__":
    resolve()

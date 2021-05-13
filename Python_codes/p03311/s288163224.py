
def main():
    from math import floor,ceil
    N = int(input())
    A = list(map(int,input().split()))
    for i in range(N):
        A[i] -= i+1
    
    def f(b):
        res = 0
        for a in A:
            res += abs(a-b)
        return res
    INF = 10**9+10
    l = -INF
    r = INF
    min_saddness = 10**15
    while l < r-2:
        m1 = (r-l)*2//3+l
        m2 = (r-l)//3+l
        tmp1 = f(m1)
        tmp2 = f(m2)

        if tmp2 < tmp1:
            r = m1
        else:
            l = m2
    print(f((l+r)//2))

main()
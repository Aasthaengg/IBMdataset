def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return a // gcd * b

def main():
    K = int(input())
    A = [int(_n) for _n in input().split()]
    maxnum = 2
    minnum = 2
    for i in reversed(range(0,K)):
        mi = (minnum + A[i] - 1)//A[i] * A[i]
        ma = maxnum // A[i] * A[i]
        # print(mi,ma)
        if mi < minnum or mi > maxnum or ma < minnum or ma > maxnum:
            print(-1)
            return
        minnum = mi
        maxnum = ma+A[i]-1
    print(minnum,maxnum)
main()
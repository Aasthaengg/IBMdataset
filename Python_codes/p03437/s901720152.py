import sys
input = sys.stdin.readline

# from collections import deque

def linput(ty=int, cnv=list):
    return cnv(map(ty, input().split()))

def vinput(rep=1, ty=int, cnv=list):
    return cnv(ty(input().rstrip()) for _ in "*"*rep)

def gcd(n,m):
    while m: n,m = m, n%m
    return n

def lcm(n,m): return n*m//gcd(n,m)

def main():
    X,Y = linput()

    res = X if X%Y else -1
    print(res)
    # sT = "No Yes".split()
    # print(sT[res])
    # for vR in mR:
    #     print(*vR, sep="")

if __name__ == "__main__":
    main()

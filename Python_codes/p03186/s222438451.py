import sys
input = sys.stdin.readline

# from collections import deque

def linput(_t=int, cnv=list):
    return cnv(map(_t, input().split()))

def gcd(n,m):
    while m: n,m = m, n%m
    return n

def lcm(n,m): return n*m//gcd(n,m)

def main():
    # N = int(input())
    # vA = [int(input()) for _ in [0,]*N]
    A,B,C = linput()
    medN, medD, poiD = A,B,C

    res = 0

    med = A+B
    deli= B+C

    # poison delicious
    if med+1 >= poiD:
        res = deli
    else:
        res = med+1 + B
        # Tak can endup with poison

    print(res)
    # print("No Yes".split()[res])

main()

import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    S=[]
    for i in range(n):
        S.append(int(input()))
    from functools import reduce
    from fractions import gcd

    def lcm(A, B):
        return A * B // gcd(A, B)


    print(reduce(lcm, S))
resolve()
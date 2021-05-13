import sys

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0:
        a, b = b, a % b
    return b

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(i) for i in input().split()]
    gcdA = A[0]
    for a in A: gcdA = gcd(gcdA, a)
    print(gcdA)

    return 0

if __name__ == "__main__":
    solve()
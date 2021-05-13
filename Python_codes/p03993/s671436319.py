import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    pair = 0
    A = [int(a) for a in input().split()]
    for i, a in enumerate(A):
        if A[a-1] == i + 1: pair += 1
    print(pair // 2)

    return 0

if __name__ =="__main__":
    solve()
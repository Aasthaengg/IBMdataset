import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort()
    L = A[N-1]
    ans = -1
    for a in A[:N-1]:
        if abs(L/2 - a) < abs(L/2 - ans): ans = a
    print(L, ans)


    return 0

if __name__ == "__main__":
    solve()
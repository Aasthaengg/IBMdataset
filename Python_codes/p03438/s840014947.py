import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]
    C = [A[i] - B[i] for i in range(N)]
    sumA = sum(A)
    sumB = sum(B)
    addA, addB = 0, 0
    for i, c in enumerate(C):
        if c > 0: addB += c
        else: addA += (-1 * c + 1) // 2
    if addA > sumB - sumA or addB > sumB - sumA: print("No")
    else: print("Yes")

    return 0

if __name__ == "__main__":
    solve()
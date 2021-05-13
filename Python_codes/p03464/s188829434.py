import sys

def solve():
    input = sys.stdin.readline
    K = int(input())
    A = [int(a) for a in input().split()]
    if A[K-1] != 2: print(-1)
    else:
        minK, maxK = 2, 3
        for i in reversed(range(K - 1)):
            mod = A[i]
            lb, hb = (minK - 1) // mod, maxK // mod
            if lb >= hb: 
                print(-1)
                break
            else:
                minK = mod * (lb + 1)
                maxK = mod * (hb + 1) - 1
        else: print(minK, maxK)

    return 0

if __name__ == "__main__":
    solve()
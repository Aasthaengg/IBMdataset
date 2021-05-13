import sys

def solve():
    input = sys.stdin.readline
    K = int(input())
    A = [int(a) for a in input().split()]
    if A[K-1] != 2: print(-1)
    else:
        minN, maxN = 2, 3
        for i in reversed(range(K - 1)):
            if maxN < A[i]: 
                print(-1)
                break
            else:
                lb = (minN - 1) // A[i]
                hb = maxN // A[i]
                if lb == hb: 
                    print(-1)
                    break
                else:
                    minN = A[i] * (lb + 1)
                    maxN = A[i] * hb + A[i] - 1
        else: print(minN, maxN)
    return 0

if __name__ == "__main__":
    solve()
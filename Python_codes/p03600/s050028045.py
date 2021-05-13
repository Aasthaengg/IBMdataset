import sys
from itertools import permutations, combinations
  
def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [[int(a) for a in input().split()] for _ in range(N)]

    length = 0
    possible = True
    for a, b in combinations(range(N), 2):
        Lab = A[a][b]
        for k in range(N):
            if k != a and k != b:
                if Lab >  A[a][k] + A[k][b]:
                    possible = False
                    break
                elif Lab ==  A[a][k] + A[k][b]:
                    break
        else: length += Lab
        if not possible:
            print(-1)
            break
    else: print(length)
    
    return 0
  
if __name__ == "__main__":
    solve()
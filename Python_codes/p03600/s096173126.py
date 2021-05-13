import sys
from itertools import permutations, combinations
  
def solve():
    input = sys.stdin.readline
    N = int(input())
    A = dict()
    for i in range(N):
        A[i] = dict()
        ain = [int(j) for j in input().split()]
        for j in range(N): A[i][j] = ain[j]

    length = 0
    possible = True
    for a, b in combinations(range(N), 2):
        Lab = A[a][b]
        create_pass = True
        for k in range(N):
            if k != a and k != b:
                if Lab >  A[a][k] + A[k][b]:
                    possible = False
                    break
                elif Lab ==  A[a][k] + A[k][b]:
                    create_pass = False
                    break
        if create_pass: length += Lab
        if not possible:
            print(-1)
            break
    else: print(length)
    
    return 0
  
if __name__ == "__main__":
    solve()

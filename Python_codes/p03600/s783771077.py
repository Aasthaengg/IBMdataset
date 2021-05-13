import sys
from itertools import combinations
  
def solve():
    input = sys.stdin.readline
    N = int(input())
    A = dict()
    for i in range(N):
        A[i] = dict()
        for j, a in enumerate(list(map(int, input().split()))): A[i][j] = a

    length = 0
    possible = True
    for a, b in combinations(range(N), 2):
        Lab = A[a][b]
        for k in range(N):
            if k != a and k != b:
                if Lab < A[a][k] + A[k][b]: continue
                if Lab >  A[a][k] + A[k][b]: possible = False
                break
        else: length += Lab
        if possible: continue
        print(-1)
        break
    else: print(length)
    
    return 0
 
if __name__ == "__main__":
    solve()

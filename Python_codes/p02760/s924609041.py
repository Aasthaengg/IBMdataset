import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)
 
def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
 
def main():
    A = [LI() for _ in range(3)]
    N = I()
    B = [I() for _ in range(N)]
    # print(B) 
    
    Hit = [[False] * 3, [False] * 3, [False] * 3]
    for i in range(3):
        for j in range(3):
            for k in range(N):
                if A[i][j]== B[k]:
                    Hit[i][j] = True
                    break
    
    ans = False
    for i in range(3):
            if (Hit[i][0] and Hit[i][1] and Hit[i][2]) or (Hit[0][i] and Hit[1][i] and Hit[2][i]):
              ans = True
              break  
    if (A[0][2] and Hit[1][1] and Hit[2][0]) or (Hit[0][0] and Hit[1][1] and Hit[2][2]):
        ans = True

    if ans:
        print('Yes')
    else:
        print('No')
main()
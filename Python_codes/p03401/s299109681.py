import sys
sys.setrecursionlimit(10000)
def resolve():
    N = int(input())
    A = list(map(int, input().split(" ")))
    A = [0] + A + [0]
    Diff = [0]
    for i in range(1, N+2):
        Diff.append(abs(A[i] - A[i-1]))
    
    total = sum(Diff)
    for i in range(1, N+1):
        print(total + abs(A[i-1] - A[i+1]) - Diff[i] - Diff[i+1])

    
if '__main__' == __name__:
    resolve()
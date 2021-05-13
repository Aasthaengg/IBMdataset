import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    T, A = [None] * N, [None] * N
    used = [False] * N
    for i in range(N):
        a, b = map(int, input().split())
        T[i] = (a + b, a, i)
        A[i] = (a + b, b, i)
    T.sort(reverse = True)
    A.sort(reverse = True)
    hapiness = 0
    ti, ai = 0, 0
    for i in range(N):
        if i % 2 == 0:
            while used[T[ti][2]]: ti += 1
            hapiness += T[ti][1]
            used[T[ti][2]] = True
            ti += 1           
        else:
            while used[A[ai][2]]: ai += 1
            hapiness -= A[ai][1]
            used[A[ai][2]] = True
            ai += 1
    print(hapiness)
   
    return 0

if __name__ == "__main__":
    solve()
import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(input()) for _ in range(N)]
    if A[0] > 0: print(-1)
    else:
        count = 0
        for i in range(1, N):
            a = A[i]
            if a <= A[i-1]: count += a
            elif a > A[i-1]:
                if a == A[i-1] + 1: count += 1
                else: 
                    print(-1)
                    break
        else: print(count)

    return 0

if __name__ == "__main__":
    solve()
def main():
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline

    N = int(input())
    A = []
    B = []
    for _ in [0]*N:
        a, b = map(int ,input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()

    if N % 2 == 0:
        median_min = (A[N//2 - 1] + A[N//2])
        median_max = (B[N//2 - 1] + B[N//2])
    else:
        median_min = A[N//2]
        median_max = B[N//2]
    print(median_max - median_min + 1)
    
main()
N = int(input())
A = sorted(map(int, input().split()))
print(A[N-1] - A[0])
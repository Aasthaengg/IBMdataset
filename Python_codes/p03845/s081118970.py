N = int(input())
A = tuple(map(int, input().split()))
M = int(input())
total = sum(A)
for _ in range(M):
    p, x = map(int, input().split())
    print(total + x - A[p - 1])
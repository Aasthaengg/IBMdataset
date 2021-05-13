N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]
c = 0
for i in range(1, N+1):
    a = A[i-1]
    c += (D - 1) // a + 1

print(c+X)
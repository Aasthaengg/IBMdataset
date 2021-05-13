N = int(input())
A = list(input().split())
A = [int(A[i]) for i in range(N)]

mother = 0

for i in range(N):
    mother += 1 / A[i]

print(1 / mother)
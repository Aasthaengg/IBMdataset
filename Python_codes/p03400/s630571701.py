N = int(input())
D, X = map(int, input().split())
Eaten = 0
A = [int(input()) for i in range(N)]
for i in range(N):
    A_i = A[i]
    Eaten += (D-1) // A_i + 1

print(X + Eaten)
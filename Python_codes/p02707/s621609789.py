N = int(input())
A = list(map(int, input().split()))
sup = [0] * N

for i in range(len(A)):
    sup[A[i]-1] += 1

for i in range(N):
    print(sup[i])

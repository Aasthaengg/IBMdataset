N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

for i in range(1, N):
    A1[i] = A1[i-1] +A1[i]

A2[0] = A1[0] + A2[0]

for j in range(1, N):
    A2[j] = max(A2[j-1] + A2[j], A2[j] + A1[j])

A = A1 + A2
print(max(A))
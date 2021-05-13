N = int(input())
A = [int(i) for i in input().split()]

A.insert(0,0)
A.append(0)

S = 0

for i in range(1,N+2):
    S += abs(A[i]-A[i-1])

for i in range(1,N+1):
    print(S + abs(A[i-1]-A[i+1]) - abs(A[i-1]-A[i]) - abs(A[i]-A[i+1]))
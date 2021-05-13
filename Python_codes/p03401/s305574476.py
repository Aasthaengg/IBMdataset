N = int(input())
A =[0] + list(map(int, input().split())) + [0]
S = 0
for i in range(N+1):
    S += abs(A[i]-A[i+1])

for i in range(1,N+1):
    Si = S + abs(A[i-1]-A[i+1]) - (abs(A[i-1]-A[i]) + abs(A[i]-A[i+1]))
    print(Si)
N = int(input())
A = list(map(int,input().split()))
cost = 0
if N == 1:
    print(0)
    exit()
for i in range(1,N):
    if A[i-1] > A[i]:
        cost += A[i-1] - A[i]
        A[i] = A[i-1]
print(cost)
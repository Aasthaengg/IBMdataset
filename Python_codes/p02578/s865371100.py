N = int(input())
A = list(map(int, input().split())) 
Ad = A.copy()
sum = 0

for i in range(N-1):
    if A[i] > A[i+1]:
        A[i+1] = A[i]

for j in range(N):
    sum += A[j]-Ad[j]

print(sum)
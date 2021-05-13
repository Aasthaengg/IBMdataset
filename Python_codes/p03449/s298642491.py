N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
max = -1
for i in range(N):
    sum = 0
    for k in range(i+1):
        sum += A[k]
    for k in range(i,N):
        sum += B[k]
    if sum > max:
        max = sum
print(max)

N = int(input())
R = {i:0 for i in range(1,N+1)}
A = list(map(int,input().split()))
for i in range(1,N+1):
    R[i] = A[i-1]
count = 0
for i in range(1,N+1):
    if i == R[R[i]]:
        count += 1
print(count//2)
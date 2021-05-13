N = int(input())
A = [int(x) for x in input().split()]
B = [int(y) for y in input().split()]
sum = 0
for i in range(N):
    sum += min(A[i],B[i])
    sum += min(max(B[i]-A[i],0),A[i+1])
    A[i+1] += max(min(A[i]-B[i],0),-A[i+1])
print(sum)

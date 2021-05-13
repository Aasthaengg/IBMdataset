import statistics 
N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    A[i] -= i
median = statistics.median(A)

sum = 0
for i in A:
    sum += abs(i-median)
print(int(sum))

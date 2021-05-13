N = int(input())
A = list(map(int,input().split()))
m = 1000
stock = 0
for i in range(N-1):
    if A[i] < A[i+1]:
        stock = m//A[i]
        m = m%A[i] + stock*A[i+1]      
print(m)
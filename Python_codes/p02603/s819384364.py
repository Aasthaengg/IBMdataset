N = int(input())
A = list(map(int, input().split()))

m = 1000
s = 0
for i in range(N):
    if i == N-1 or A[i] > A[i+1]: 
        m += s * A[i]
        s = 0
    elif A[i] < A[i+1]:
        x = m // A[i]
        s += x
        m -= x * A[i]
print(m)
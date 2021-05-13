N = int(input())
A = [int(i) for i in input().split()]

m = 1000
s = 0
for i in range(N-1):
    if A[i] > A[i+1]:
        m += s*A[i]
        s = 0
    else:
        s += m//A[i]
        m %= A[i]

print(m+s*A[-1])

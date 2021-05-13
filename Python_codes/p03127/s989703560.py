n = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
    while b != 0:
        c = a%b
        a = b
        b = c
    return a

for i in range(1, n):
    A[i] = gcd(A[i-1], A[i])
print(A[-1])
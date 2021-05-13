from fractions import gcd
N = int(input())
A = tuple(map(int, input().split()))

l = A[0]
for i in range(1, N):
    l = l * A[i] // gcd(l, A[i])
l = l - 1

f = 0 
for a in A:
    f += l % a
print(f)

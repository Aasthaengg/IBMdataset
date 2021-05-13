N, T = map(int, input().split())
A = [int(i) for i in input().split()]

c = 0
MAX = 0
a1 = A[0]
for i in range(N-1):
    if A[i] <= a1:
        a1 = A[i]
    a2 = A[i+1]
    if MAX == a2 - a1:
        c += 1
    elif MAX < a2 - a1:
        MAX = a2 - a1
        c = 1
print(c)

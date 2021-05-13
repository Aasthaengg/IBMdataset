N = int(input())
A = sorted([int(a) for a in input().split()])
print(A[-1]-A[0]+sum([abs(a) for a in A[1:-1]]))

p = A[-1]
for i in range(N-1):
    a, b = max(p, A[i]), min(p, A[i])
    if i == N-2 or A[i+1] < 0:
        print(a, b)
        p = a - b
    else:
        print(b, a)
        p = b - a
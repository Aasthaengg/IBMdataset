N = int(input())
A = list(map(int, input().split()))

A = sorted([a-i-1 for i, a in enumerate(A)])
i = int(len(A)/2)
b = A[i]

print(sum([abs(a-b) for a in A]))
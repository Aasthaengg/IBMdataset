N = int(input())
A = sorted(list(map(int, input().split())))

i = A.pop()
j = None
best = float('inf')

for a in A:
    v = abs(a - i / 2)
    if v < best:
        best = v
        j = a

print(i, j)

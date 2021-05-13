n, l = map(int, input().split())

a = []
b = float('inf')
for i in range(1,n+1):
    a.append(i+l-1)
    if abs(i+l-1) < b:
        c = i+l-1
        b = abs(i+l-1)

A = sum(a)

print(A-c)
n = int(input())

A, B = 0, 0
for i in range(n):
    a, b = map(int, input().split())
    if a > A:
        A, B = a, b

print(A+B)

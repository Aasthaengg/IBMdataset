A, B, C = map(int, input().split())
m = max(A, B, C)
print(m * 9 + sum((A, B, C)))
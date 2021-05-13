A, B, C = map(int, input().split())

a = A - B
print(C - a if C - a > 0 else 0)
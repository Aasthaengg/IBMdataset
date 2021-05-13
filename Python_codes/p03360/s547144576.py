A, B, C = map(int, input().split())
K = int(input())
s = A + B + C
m = max(A, B, C)
print(s + (2**K - 1) * m)
A, B, C = map(int, input().split())
m = max(A, B, C)
k = m*3-A-B-C
print((k+3)//2 if k%2 else k//2)
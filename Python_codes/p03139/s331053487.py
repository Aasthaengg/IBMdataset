N, A, B = map(int, input().split())
maxv = min(A, B)
if A+B-N >= 0:
    minv = A+B-N
else:
    minv = 0
print(maxv, minv)
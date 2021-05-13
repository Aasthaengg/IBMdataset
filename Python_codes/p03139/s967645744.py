N, A, B = map(int, input().split())
maxv = min(A, B)
minv =  max(0, maxv - (N-max(A, B)))
print(maxv, minv)
N, A, B = map(int, input().split())

ma = str(min(A,B))
if A+B-N > 0:
    mi = str(A + B - N)
else:
    mi = str(0)
print(ma+' '+mi)

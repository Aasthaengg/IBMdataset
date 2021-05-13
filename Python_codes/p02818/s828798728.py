A, B, K = map(int,input().split())
if K>A and K<(A+B):
    B = B-(K-A)
    l = [0,B]
elif K>A and K>=(A+B):
    l = [0, 0]
else:
    l = [A-K,B]
print(' '.join(map(str, l)))

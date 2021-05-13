A, B, C, K = list(map(int, input().split()))

res = 0
if K <= A:
    res = K
elif K <= B:
    res = A
else:
    res = A - (K - A - B)

print(res)

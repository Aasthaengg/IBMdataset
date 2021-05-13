# B - Tax Rate
ans = ':('
N = int(input())
for X in range(1,50000):
    tmp = int(X*1.08+0.000001)
    if tmp==N:
        ans = X
        break
print(ans)
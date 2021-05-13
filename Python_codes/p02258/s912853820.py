maxv = -1 * (10 ** 10) - 1
minv = 10 ** 10 + 1

n = int(input())

for i in range(n):
    tmp = int(input())
    
    maxv = max(maxv, tmp - minv)
    minv = min(tmp, minv)

print(maxv)
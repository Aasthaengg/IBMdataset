A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
minnum = float('inf')
for i in range(M):
    x, y, z = map(int, input().split())
    minnum = min(a[x-1] + b[y-1] - z, minnum)

print(min(minnum, min(a) + min(b)))
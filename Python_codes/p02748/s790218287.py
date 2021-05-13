A, B, M = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = min(a)+min(b)
m = []
for i in range(M):
    x, y, c = list(map(int, input().split()))
    tmp = a[x-1] + b[y-1] - c
    if res > tmp:
        res = tmp
print(res)
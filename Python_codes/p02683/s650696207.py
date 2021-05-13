n, m, x = map(int, input().split())

a = [[0] * m for j in range(n)]
c = [0] * n

ans = 10**10

for i in range(n):
    arr = list(map(int, input().split()))
    c[i] = arr[0]
    a[i] = arr[1:]

# bit全探索
import itertools
for bit in itertools.product([0,1], repeat=n):
    arr = [0] * m
    cost = 0
    for i in range(n):
        if bit[i] == 1:
            for k in range(len(a[i])):
                arr[k] += a[i][k]
            cost += c[i]

    NG = False
    for i in range(len(arr)):
        if arr[i] < x:
            NG = True
            
    if NG:
        pass
    else:
        ans = min(ans,cost)

if ans != 10**10:
    print(ans)
else:
    print(-1)

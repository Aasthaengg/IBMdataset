A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cost = [0] * M
for i in range(M) :
    x, y, c = map(int, input().split())
    cost[i] = a[x-1] + b[y-1] - c
a = sorted(a) ; b = sorted(b)
print(min(min(cost),a[0]+b[0]))

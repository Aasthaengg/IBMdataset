A, B, M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

mini = float('inf')

for i in range(M):
    x, y, c = map(int,input().split())
    if a[x-1] + b[y-1] - c < mini:
        mini = a[x-1] + b[y-1] - c

if min(a) + min(b) < mini:
    print(min(a) + min(b))
else:
    print(mini)


A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
xyc = [list(map(int, input().split())) for i in range(M)]

smallest = min(a) + min(b)

for i in range(M):
    if a[xyc[i][0]-1] + b[xyc[i][1]-1] - xyc[i][2] < smallest:
        smallest = a[xyc[i][0]-1] + b[xyc[i][1]-1] - xyc[i][2]

print(smallest)

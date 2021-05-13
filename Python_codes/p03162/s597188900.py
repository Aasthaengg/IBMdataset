n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

a = [0] * n
b = [0] * n
c = [0] * n

a[0], b[0], c[0] = l[0][0], l[0][1], l[0][2]

for i in range(1,n):
    a[i] = max(l[i][0]+b[i-1], l[i][0]+c[i-1])
    b[i] = max(l[i][1]+a[i-1], l[i][1]+c[i-1])
    c[i] = max(l[i][2]+a[i-1], l[i][2]+b[i-1])

print(max(a[-1],b[-1],c[-1]))
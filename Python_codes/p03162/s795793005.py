n = int(input())

a = [0]*n
b = [0]*n
c = [0]*n

days = [0]*n
for i in range(n):
    days[i] = list(map(int, input().split()))

a[0], b[0], c[0] = days[0][0], days[0][1], days[0][2]

for i in range(1, n):
    a[i] = max(b[i-1]+days[i][0], c[i-1]+days[i][0])
    b[i] = max(a[i-1]+days[i][1], c[i-1]+days[i][1])
    c[i] = max(a[i-1]+days[i][2], b[i-1]+days[i][2])

print(max(a[-1], b[-1], c[-1]))
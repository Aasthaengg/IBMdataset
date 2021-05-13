k, x = map(int, input().split())
n = k - 1
data = []
for i in range(1, n+1):
    data.append( x - i )
data.append(x)
for i in range(1, n+1):
    data.append( x + i )

data.sort()

print(*data)

import math
N = int(input())
x = []
y = []

for i in range(N):
    xi, yi = map(int, input().split(" "))
    x.append(xi)
    y.append(yi)


route = 0
for i in range(N):
    for j in range(i, N):
        route += math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)

# print(route * math.factorial(N-1) * 2 / math.factorial(N))
print(route * 2 / N)

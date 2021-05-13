n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = [abs(x[i] - y[i]) for i in range(n)]
dist_1 = 0.
dist_2 = 0.
dist_3 = 0.
dist_infty = float(max(z))
for i in range(n):
    dist_1 += z[i]
    dist_2 += z[i] ** 2
    dist_3 += z[i] ** 3
dist_2 = pow(dist_2, 1 / 2.)
dist_3 = pow(dist_3, 1 / 3.)
print(dist_1, dist_2, dist_3, dist_infty, sep='\n')
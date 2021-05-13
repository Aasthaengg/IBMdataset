n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

xy_abs = [abs(x[i] - y[i]) for i in range(n)]
manhattan_distance = sum(xy_abs)
euclid_distance = sum([xy ** 2 for xy in xy_abs]) ** 0.5
p3_distance = sum([xy ** 3 for xy in xy_abs]) ** (1/3)
chebyshev_distance = max(xy_abs)

print(manhattan_distance)
print(euclid_distance)
print(p3_distance)
print(chebyshev_distance)



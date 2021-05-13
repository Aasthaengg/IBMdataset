n, k = map(int, input().split())
x_list = list(map(int, input().split()))

min_dist = float('inf')
for i in range(0, n-(k-1)):
    left = x_list[i]
    right = x_list[i+(k-1)]

    dist = abs(left - right) + min(abs(left), abs(right))
    min_dist = min(dist, min_dist)
print(min_dist)

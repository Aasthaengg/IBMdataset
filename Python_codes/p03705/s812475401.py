n, a, b = map(int, input().split())

max_sum = b*(n-1)+a
min_sum = a*(n-1)+b

if max_sum - min_sum >= 0:
    print(max_sum - min_sum + 1)
else:
    print(0)
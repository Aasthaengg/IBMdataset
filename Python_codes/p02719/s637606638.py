n, k = [int(x) for x in input().split()]
print(min(n % k, -n % k))
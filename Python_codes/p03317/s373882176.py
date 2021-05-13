n, k = map(int, input().split())
A = tuple(map(int, input().split()))
count = -(-(n - 1) // (k-1))
print(count)
n, k = map(int, input().split())
a = [int(i) for i in input().split()]
print(1 if n <= k else 1 + -(-(n - k) // (k - 1)))
n, k = map(int, input().split())
a = sorted(map(int, input().split()))
print(sum(a[0 : max(0, n - k)]))

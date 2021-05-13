n, m = map(int, input().split())
a = list(map(int, input().split()))
print(n - sum(a) if 0 <= n - sum(a) else '-1')
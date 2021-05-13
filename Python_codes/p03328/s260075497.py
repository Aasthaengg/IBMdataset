a, b = map(int, input().split())
sub = b - a - 1
n = sub * (sub + 1) // 2
print(n - a)
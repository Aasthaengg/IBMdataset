_, *a = map(int, open(0).read().split())
n = max(a)
print(n, min((abs(n/2 - i), i) for i in a)[1])
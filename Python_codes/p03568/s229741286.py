n, *a = map(int, open(0).read().split())
print(3**n - 2**sum(1-i%2 for i in a))
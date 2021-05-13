n, *a = map(int, open(0).read().split())
print(len([i for i, v in enumerate(a) if -~i & v & 1]))

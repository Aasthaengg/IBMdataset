n, *a = map(int, open(0).read().split())
print(sum(i < j < k < i + j for k in a for j in a for i in a))
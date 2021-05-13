N, *A = map(int, open(0).read().split())

print(len([a for a in A[::2] if a%2]))
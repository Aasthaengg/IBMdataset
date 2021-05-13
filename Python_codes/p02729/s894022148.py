a = input().split()
N = int(a[0])
M = int(a[1])

kotae = int(N * (N - 1) / 2)
kotae2 = int(M  * (M - 1) / 2)

print(kotae + kotae2)
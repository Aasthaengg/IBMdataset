N = int(input())
A = int(input())

_, m = divmod(N, 500)

print('Yes' if m <= A else 'No')
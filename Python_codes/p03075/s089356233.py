*A, k = map(int, open(0).read().split())

max_diff = max(A) - min(A)

if max_diff <= k:
    print("Yay!")
else:
    print(":(")
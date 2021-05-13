n, k = map(int, input().split())
As = list(map(int, input().split()))

idx = As.index(min(As))
left = idx

n_l = (left + k - 2) // (k - 1)

right = n - ((n_l) * (k-1)) - 1

n_r = (right + k - 2) // (k - 1)

print(n_l + n_r)
n = int(input())
mod = int(1e9)+7
bad = pow(9, n, mod) * 2 - pow(8, n, mod)
good = pow(10, n, mod)
print((good - bad) % mod)

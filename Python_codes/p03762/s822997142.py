n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10**9 + 7

def main(n, x, mod):
    w = 0
    for i in range(1, n):
        w += (x[i] - x[i-1]) * i * (n-i)
        w %= mod
    return w

print(main(n, x, mod) * main(m, y, mod) % mod)
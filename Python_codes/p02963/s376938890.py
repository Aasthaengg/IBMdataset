s = int(input())
mod = 10 ** 9
x = (mod - s % mod) % mod
y = (s+x) // mod
print(0, 0, mod, 1, x,y)

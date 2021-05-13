N = int(input())
p = 1
mod = 10 ** 9 + 7
for i in range(N):
    p *= i + 1
    p %= mod

print(p)

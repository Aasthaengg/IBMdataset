s = int(input())
MOD = 10**9
x = (-s) % MOD
y = (s+x)//MOD
print(0, 0, 10**9, 1, x, y)
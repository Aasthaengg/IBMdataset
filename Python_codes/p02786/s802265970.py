H = int(input())

res = 0
n = 1
while H > 0:
    res += n
    H //= 2
    n *= 2

print(res)
alfa = "0abcdefghijklmnopqrstuvwxyz"
N = int(input())
n = N
res = ""
while True:
    x = n % 26
    if x == 0:
        x = 26
    res += alfa[x]
    n -= x
    if n == 0:
        break
    n //= 26
print(res[::-1])
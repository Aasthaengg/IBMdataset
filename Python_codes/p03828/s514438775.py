import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
Mod = 10 ** 9 + 7

# 素因数分解(prime factorize)
def prime_factorize(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

n = int(readline())

p_list = [0] * (n + 1)

for i in range(2, n + 1):
    arr = prime_factorize(i)
    for p, e in arr:
        p_list[p] += e

ans = 1
for j in p_list:
    if j >= 1:
        ans *= (j + 1)
        ans %= Mod
print(ans)
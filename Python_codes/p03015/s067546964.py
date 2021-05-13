#%%
n = list(input())
n = n[::-1]
if n.count('1') == len(n):
    n = list('0' * len(n) + '1')
else:
    for i in range(len(n)):
        if n[i] == '0':
            n[i] = '1'
            point = i
            break
    for i in range(point):
        n[i] = '0'

n = n[::-1]

count = 0
ans = 0
mod = 10 ** 9 + 7

for i in range(len(n)):
    a = pow(2, count, mod)
    b = pow(3, len(n)-i-1, mod) 
    tmp = (a * b) % mod
    if n[i] == '1':
        count += 1
        ans += tmp
        ans %= mod

print(ans)
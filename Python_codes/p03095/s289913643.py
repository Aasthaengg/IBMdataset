n = int(input())
s = input()
mod = 10 ** 9 + 7

dict = {ch: 0 for ch in 'abcdefghijklmnopqrstuvwxyz'}
for i in range(n):
    dict[s[i]] += 1

ans = 1
for x in dict.values():
    ans = ans * (x+1) % mod
print((ans - 1) % mod)
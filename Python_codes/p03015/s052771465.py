L = input()[1:]
mod = 10**9 + 7

sure = 1
possible = 2
for bit in L:
    if bit == '1':
        sure = (sure * 3 + possible) % mod
        possible = possible * 2 % mod
    else:
        sure = sure * 3 % mod

ans = (sure + possible) % mod
print(ans)
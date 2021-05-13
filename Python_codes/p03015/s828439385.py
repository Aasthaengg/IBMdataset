L = input()
mod = 10**9 + 7

x = len(L)
L = int(L, 2)
sure = 1
possible = 2
for i in range(2, x+1):
    if (L >> (x-i)) & 1:
        sure = (sure * 3 + possible) % mod
        possible = possible * 2 % mod

    else:
        sure = sure * 3 % mod
        
ans = (sure + possible) % mod
print(ans)
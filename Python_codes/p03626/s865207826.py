n = int(input())
s1 = input()
s2 = input()
mod = 1000000007

if n == 1 or s1[0] != s1[1]:
    ans = 3
    ind = 1
    mae = 1
else:
    ans = 6
    ind = 2
    mae = 2

while ind < n-1:
    if s1[ind] == s1[ind + 1]:
        if mae == 2:
            ans = (ans * 3) % mod
        else:
            ans = (ans * 2) % mod
        ind += 2
        mae = 2
    else:
        if mae == 2:
            ans = (ans * 1) % mod
        else:
            ans = (ans * 2) % mod
        ind += 1
        mae = 1

if ind == n-1:
    if mae == 2:
        ans = (ans * 1) % mod
    else:
        ans = (ans * 2) % mod

print(ans % mod)

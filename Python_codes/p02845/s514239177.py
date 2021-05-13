MOD = 10**9 + 7
n = int(input())
x, y, z = 0, 0, 0
ans = 1
for a in map(int, input().split()):
    if a == x:
        if x != y:
            x += 1
        elif y != z:
            ans = ans * 2 % MOD
            y += 1
        else:
            ans = ans * 3 % MOD
            z += 1
    elif a == y:
        if y != z:
            y += 1
        else:
            ans = ans * 2 % MOD
            z += 1
    elif a == z:
        z += 1
    else:
        ans = 0
print(ans)
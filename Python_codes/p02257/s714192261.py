from math import sqrt
n = int(input())
ans = 0
for i in range(n):
    x = int(input())
    ok = 1
    for z in range(2, int(sqrt(x))+1):
        if x % z == 0:
            ok = 0
            break
    ans += ok
print(ans)
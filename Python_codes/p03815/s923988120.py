x = int(input())

ans = 0

if x >= 11:
    t = x//11
    ans += t*2
    x = x%11

if x > 6:
    ans += 2
elif x <= 6 and x != 0:
    ans += 1

print(ans)
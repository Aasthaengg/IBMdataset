x = int(input())

if x <= 6:
    ans = 1
elif 6 < x < 11:
    ans = 2
elif x%11 == 0:
    ans = (x//11)*2
else:
    ans = (x//11)*2
    x = x%11
    if x <= 6:
        ans += 1
    else:
        ans += 2

print (ans)

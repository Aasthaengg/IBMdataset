ans = 0
now = 0 # # of red blocks left
for c in input():
    if c == '1':
        if now > 0:
            ans += 2
        now -= 1
    else:
        if now < 0:
            ans += 2
        now += 1
print(ans)

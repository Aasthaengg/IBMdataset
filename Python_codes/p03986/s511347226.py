l = 0
ans = 0
for c in input():
    if c == 'S':
        l += 1
    else:
        if l == 0:
            ans += 1
        else:
            l -= 1
print(ans + l)

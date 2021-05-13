s = input()
p, g = 0, 0
ans = 0
for e in s:
    if e == "g":
        if p < g:
            p += 1
            ans += 1
        else:
            g += 1
    else:
        if p < g:
            p += 1
        else:
            g += 1
            ans -= 1
print(ans)

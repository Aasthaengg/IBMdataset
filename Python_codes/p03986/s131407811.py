x = input()
s = 0
ans = 0
for c in x:
    if c == 'S':
        s += 1
    else:
        if s == 0:
            ans += 2
        else:
            s -= 1
print(ans)

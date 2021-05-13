s = input().replace("BC","D")
ans = 0
c = 0
for e in s:
    if e == "A":
        c += 1
    elif e == "D":
        ans += c
    else:
        c = 0
print(ans)

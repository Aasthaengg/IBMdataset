X = input()
ans = 0
sc = 0
for x in X:
    if x == "S":
        sc += 1
    else:
        if sc:
            sc -= 1
        else:
            ans += 2
print(ans)
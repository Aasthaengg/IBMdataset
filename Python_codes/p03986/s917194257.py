X = input()

ans = len(X)
s = 0
for x in X:
    if x == "S":
        s += 1
    else:
        if s:
            ans -= 2
            s -= 1
print(ans)
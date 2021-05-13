X = input()
ans = len(X)
sc = 0
for x in X:
    if x == "S":
        sc += 1
    elif sc > 0:
        sc -= 1
        ans -= 2
print(ans)

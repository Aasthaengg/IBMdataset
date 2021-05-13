X = input()
ans = len(X)
c = 0

for x in X:
    if x == 'S':
        c += 1
    else:
        if c > 0:
            ans -= 2
            c -= 1
print(ans)
X = input()
ans, sc = 0, 0
for x in X:
    if x == 'T':
        sc += 1
    else:
        sc -= 1
    ans = max(ans, sc)
print(ans*2)

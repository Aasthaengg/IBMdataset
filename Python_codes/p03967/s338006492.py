S = input()

ans = 0
for i,c in enumerate(S):
    if i%2==0:
        if c=='p':
            ans -= 1
    else:
        if c=='g':
            ans += 1
print(ans)
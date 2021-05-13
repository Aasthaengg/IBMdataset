S = input()

ans = 0
for i,c in enumerate(S):
    if i%2 and c=='g':
        ans += 1
    elif i%2==0 and c=='p':
        ans -= 1
print(ans)
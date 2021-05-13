S = input()
ans = 0
while len(S)>=2:
    if S[0]==S[-1]:
        S = S[1:-1]
    elif S[0]=='x':
        ans += 1
        S = S[1:]
    elif S[-1]=='x':
        ans += 1
        S = S[:-1]
    else:
        ans = -1
        break
print(ans)
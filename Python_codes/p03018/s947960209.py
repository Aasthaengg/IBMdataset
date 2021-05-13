S = list(input())
N = len(S)

if S[0] == 'A':
    ac = 1
else:
    ac = 0

ans = 0
for i in range(1,N):
    if S[i] == 'A':
        if S[i-1] != 'A':
            ac = 1
        else:
            ac += 1
    elif S[i] == 'B':
        if S[i-1] != 'A':
            ac = 0
    else:
        if S[i-1] == 'B':
            ans += ac
            S[i] = 'A'
        else:
            ac = 0

print(ans)


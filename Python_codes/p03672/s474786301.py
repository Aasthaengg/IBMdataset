S = input()[:-1]
ans = 0

for i in range(len(S)):
    if S[:len(S)//2] == S[len(S)//2:]:
        ans = len(S)
        break
    else:
        S = S[:-1]
print(ans)
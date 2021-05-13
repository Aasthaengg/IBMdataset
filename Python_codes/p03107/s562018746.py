S = input()
ans = 0
i = 0
while i < len(S)-1:
    if S[i] != S[i+1]:
        ans += 2
        if i==0:
            S = S[2:]
        else:
            S = S[:i] + S[i+2:]
            i -= 1
    else:
        i += 1
print(ans)

S = input()
ans = 0
for i in range(2**(len(S)-1)):
    moji = S[0]
    tmp = 0
    for j in range(len(S)-1):
        if ((i >>j) & 1):
            moji = moji + '+' + S[j +1]
        else:
            moji = moji + S[j+1]
    tmp = moji.split('+')
    for k in range(len(tmp)):
        ans += int(tmp[k])
print(ans)

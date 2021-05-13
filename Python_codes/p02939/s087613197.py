#参考にしたい解答
S = input() 
i= 0
ans = 0
moji1 = ""
moji2 = ""
while i < len(S):
    if i == 0:
        moji1 = S[i]
        ans += 1
    else:
        moji2 = moji2 + S[i]
        if moji1 != moji2:
            ans += 1
            moji1 = moji2
            moji2 = ""
        else:
            moji2 = moji2 + S[i]
    i += 1
 
print(ans)
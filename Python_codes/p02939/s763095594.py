S = input()

i = 1
buf = S[0]
ans = 1

while i <= len(S) - 1:
    if buf == S[i]:
        # 2文字ずらすと，何をとってもOK (Siは2文字，Si+1は1文字なので)
        i = i + 2
        if i <= len(S): # ズラした分，末尾じゃなければ+1
            ans += 1
        buf = ""
    else:
        # 違う文字ならそのまま入れ替えればOK
        ans += 1
        buf = S[i]
        i = i + 1

print(ans)
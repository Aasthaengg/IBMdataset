S = input()
cnt = 1
tf = False
a = S[0]

for i in range(1, len(S)):
    if tf:
        cnt += 1
        a = S[i-1] + S[i]
        tf = False
    else:
        if a == S[i]:
            tf = True
        else:
            cnt += 1
            a = S[i]

print(cnt)
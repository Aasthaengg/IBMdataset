## A - Dividing a String
S = list(input())
x = ''
chk = ''
cnt = 0
for i in range(len(S)):
    chk += S[i]
    if x != chk:
        x = chk
        chk = ''
        cnt += 1    
print(cnt)
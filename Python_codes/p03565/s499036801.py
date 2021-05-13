S = input()
T = input()
t = len(T)
if len(S) < t :
    print('UNRESTORABLE')
    exit()
ans = []
for i in range(len(S)-t+1) :
    s = S[i:i+t]
    if all (s[j] == '?' or s[j] == T[j] for j in range(t)) :
        x = (S[:i]+ T + S[i+t:]).replace('?','a')
        ans.append(x)

if ans :
    ans.sort()
    print(ans[0])
else :
    print('UNRESTORABLE')
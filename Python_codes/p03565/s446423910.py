S = input()
T = input()

if len(S) < len(T):
    print('UNRESTORABLE')
    exit()

ans = 'z'*51
for i in range(len(S)-len(T)+1):
    s = S[i:i+len(T)]
    for a,b in zip(s,T):
        if a==b or a=='?': continue
        break
    else:
        cand = S[:i] + T + S[i+len(T):]
        ans = min(ans, cand.replace('?','a'))

print('UNRESTORABLE' if ans=='z'*51 else ans)
S = input()
T = input()
ans = []

lt = len(T)
for i in range(len(S)-lt+1):
    s = S[i:i+lt]
    for t in range(lt):
        if s[t]=='?':
            if t != lt-1:
                pass
            else:
                ans.append((S[:i]+T+S[i+lt:]).replace('?', 'a'))
        else:
            if s[t]!=T[t]:
                break
            elif t==lt-1:
                ans.append((S[:i]+T+S[i+lt:]).replace('?', 'a'))
                break

print(min(ans) if len(ans)>0 else "UNRESTORABLE")
S = input()
S=S[::-1]

s = ['dream','dreamer','erase','eraser'] 
s = [_[::-1] for _ in s]

idx = 0
ans='YES'
while idx < len(S):
    if S[idx] == 'm':
        if S[idx:idx+5] == s[0]:
            idx=idx+5
        else:
            ans='NO'
            break
        
    elif S[idx] == 'e':
        if S[idx:idx+5] == s[2]:
            idx=idx+5
        else:
            ans='NO'
            break
        
    elif S[idx] == 'r':
        if S[idx:idx+7] == s[1]:
            idx=idx+7
        elif S[idx:idx+6] == s[3]:
            idx=idx+6
        else:
            ans='NO'
            break
        
    else:
        ans='NO'
        break
        
print(ans)

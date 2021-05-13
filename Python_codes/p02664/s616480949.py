s = list(input())
if s[0] == '?':
    s[0] = 'D'
if s[-1] == '?':
    s[-1] = 'D'
    
for i in range(1, len(s)):
    if s[i] == '?':
        if s[i-1] == 'P':
            s[i] = 'D'
        elif s[i-1] == 'D':
            if s[i+1] == 'P':
                s[i] = 'D'
            else:
                s[i] = 'P'
            
print(''.join(s))
s = list(input())
t = list(input())

for i in range(len(s)-len(t), -1, -1):
    flag = True
    for j in range(len(t)):
        if not(s[i+j] == t[j] or s[i+j] == '?'):
            flag = False 
    if flag :
        for j in range(len(t)):
            s[i+j] = t[j]
        for k in range(len(s)):
            if s[k] == '?':
                s[k] = 'a'
        print(''.join(s))
        exit()
print('UNRESTORABLE')

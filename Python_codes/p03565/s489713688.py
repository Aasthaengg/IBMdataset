s=input()
t=input()
if len(s)<len(t):
    print('UNRESTORABLE')
    exit()
for i in range(len(s)-len(t),-1,-1):
    for j in range(len(t)):
        if s[i+j]!='?' and s[i+j]!=t[j]:
            break
    else:
        print(s[:i].replace('?','a')+t+s[i+len(t):].replace('?','a'))
        break
else:
    print('UNRESTORABLE')
s=sorted(input())
t=sorted(input())[::-1]
A=True
for i in range(min(len(s),len(t))):
    if s[i]<t[i]:
        A = True
        break
    elif s[i]>t[i]:
        A = False
        break
    else:
        if len(s)<len(t): A=True
        else:A= False
print('Yes' if A else 'No')
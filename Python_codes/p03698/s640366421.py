s=input()
Flag=True
for i in range(len(s)):
    num=s.count(s[i])
    if num>1:
        Flag=False
if Flag:
    print('yes')
else:
    print('no')
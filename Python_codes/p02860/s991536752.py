n =input()
s=input()
if len(s)%2==0:
    if s[len(s)//2:] == s[:len(s)//2]:
        print('Yes')
    else:
        print('No')
else:
    print('No')
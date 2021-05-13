s=input()

if 'C' in s:
    A=s.index('C')
    for i in range(A,len(s)):
        if s[i]=='F':
            print('Yes')
            break
    else:
        print('No')
else:
    print('No')
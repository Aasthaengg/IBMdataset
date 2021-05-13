import sys
s=input()
for k in range(len(s)):
    if s[k]=='C':
        for l in range(k+1,len(s)):
            if s[l]=='F':
                print('Yes')
                sys.exit()
else:
    print('No')
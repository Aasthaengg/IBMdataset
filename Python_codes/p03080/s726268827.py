N = int(input())
s = input()
s = s.replace('R','')
if(len(s)<N-len(s)):
    print('Yes')
else:
    print('No')
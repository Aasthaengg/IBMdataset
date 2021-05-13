s = str(input())
s1 = sorted(s)

if s1[0]==s1[1] and s1[1]!=s1[2] and s1[2]==s1[3]:
    print('Yes')
else:
    print('No')
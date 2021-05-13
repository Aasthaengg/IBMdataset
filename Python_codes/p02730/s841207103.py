import sys
s = input()
pre = []
back = []
for i in range((len(s)-1)//2):
    pre.append(s[i])
s1 = ''.join(pre)

for i in range((len(s)+3)//2-1,len(s)):
    back.append(s[i])
s2 = ''.join(back)

if s != s[::-1]:
    print('No')
    sys.exit()
elif s1 != s1[::-1]:
    print('No')
    sys.exit()
elif s2 != s2[::-1]:
    print('No')
    sys.exit()
print('Yes')
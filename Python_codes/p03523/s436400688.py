s = input()
ans=[]
for i in range(len(s)):
    if s[i]!='A':
        ans+=s[i]

if ''.join(ans)=='KIHBR' and len(s)<=9 and 'AA' not in s and 'AAA' not in s and 'AAAA' not in s and 'KIH' in s:
    print('YES')
else:
    print('NO')
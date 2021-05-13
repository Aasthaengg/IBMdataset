s=input()
if s[0] != 'A':
    print('WA')
    exit()
if s[2:len(s)-1].count('C') != 1:
    print('WA')
    exit()
for i in range(1,len(s)):
    if s[i]=='C':
        continue
    if s[i].isupper() == True:
        print('WA')
        exit()
print('AC')
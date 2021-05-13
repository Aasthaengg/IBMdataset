s=input()
if len(s)%2:
    print('No')
    exit()
for i in range(0,len(s),2):
    if i > len(s):
        break
    if s[i] != 'h' or s[i+1]!='i':
        print('No')
        exit()
print('Yes')
a=list(input())

if a[0]!='A' or 'C' not in a[2:-1]:
    print('WA')
    exit()
a.remove('A')
a.remove('C')
n=''.join(a)
if n.islower()==False:
    print('WA')
    exit()
print('AC')
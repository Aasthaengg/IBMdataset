s = input()
n = len(s)
if n % 2:
    print('No')
    exit()

for i in range(0,n-1,2):
    if s[i:i+2] != 'hi':
        print('No')
        exit()
print('Yes')

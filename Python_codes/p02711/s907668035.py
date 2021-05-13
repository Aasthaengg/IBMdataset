import sys
n = list((input()))
for i in range(3):
    if n[i] == '7':
        print('Yes')
        sys.exit()
print('No')
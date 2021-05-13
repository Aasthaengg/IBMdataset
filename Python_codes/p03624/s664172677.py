import string
import sys
s = str(input())
low = string.ascii_lowercase
fin = ''
for i in range(len(low)):
    if low[i] not in s:
        print(low[i])
        sys.exit()
print('None')

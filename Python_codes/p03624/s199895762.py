import string
s = str(input())
low = string.ascii_lowercase
fin = ''
for i in range(len(low)):
    if low[i] not in s:
        fin += low[i]
if len(fin) == 0:
    print('None')
else:
    print(fin[0])
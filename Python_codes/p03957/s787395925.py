import sys
s=str(input())
c=0
for i in s:
    if i=='C':
        c=1
    if i=='F' and c==1:
        print('Yes')
        sys.exit()

print('No')
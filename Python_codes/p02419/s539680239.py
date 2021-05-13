import re
c=0
s=''
p=input().upper()
ptn=re.compile(r'^'+p+r'$')

while True:
    s=input()
    if s =='END_OF_TEXT':
        break
    a=s.upper().split()
    for i in a:
        if re.match(ptn, i):
            c+=1
print(c)
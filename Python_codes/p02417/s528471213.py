
import sys
a=[]
for i in sys.stdin.readlines():
    a.append(i.rstrip())
    
b=''.join(a)
x=str.lower(b)

for i in "abcdefghijklmnopqrstuvwxyz":
    countable=x.count(i)
    print(f'{i} : {countable}')

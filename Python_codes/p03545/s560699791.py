import sys
import itertools

a, b, c, d = list(input())

lst = ['-', '+']
for i, j, k in itertools.product(range(2), range(2), range(2)):
    ans = int(a)
    if i:
        ans += int(b)
    else:
        ans -= int(b)
    if j:
        ans += int(c)
    else:
        ans -= int(c)
    if k:
        ans += int(d)
    else:
        ans -= int(d)
        
    if ans == 7:
        print(a,lst[i],b,lst[j],c,lst[k],d,'=7',sep='')
        break
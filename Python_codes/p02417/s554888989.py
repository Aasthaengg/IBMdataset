x=[]
while True:
    try:
        z=list(input())
    except EOFError:
        break
    x=x+z
import collections
c=collections.Counter(x)
import string
a=string.ascii_letters
for i in range(26):
    print(a[i],":",(c[a[0+i]]+c[a[26+i]]))

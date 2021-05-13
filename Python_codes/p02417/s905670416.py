c=[]
S=[]
lst=[]
import string
a=string.ascii_letters
import collections
try:
    while True:
        lst=lst+list(input())
        
        #S += collections.Counter(c)
except EOFError:
    pass
c = collections.Counter(lst)

for i in range(26):
    print(a[i]+" : "+str(c[a[0+i]]+c[a[26+i]]))


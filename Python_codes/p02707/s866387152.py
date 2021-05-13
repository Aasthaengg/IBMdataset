n = int(input())
a = list(map(int, input().split()))

import collections

c = collections.Counter(a) 


for k in range(1,n+1):
    try: 
        print(c[k])
    except:
        print(0)
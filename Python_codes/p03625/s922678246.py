N = int(input())
A = list(map(int, input().split()))

import collections
lst=collections.Counter(A).most_common()
lst_larger=[el for el in lst if el[1]>=2]
#print(lst)
#print(lst_larger)
if len(lst_larger) >= 2:
    lst_larger=sorted(lst_larger, key=lambda x:x[0], reverse=True)
    if lst_larger[0][1]>=4:
        print(lst_larger[0][0]**2)
    else:
        print(lst_larger[0][0]*lst_larger[1][0])
else:
    print(0)

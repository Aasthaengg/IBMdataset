import copy
n=int(input())
li=[int(input()) for i in range(n)]
la=copy.copy(li)
la.sort()
m=la[-1]
for i in li:
    if i==m:
        print(la[-2])
    else:
        print(m)

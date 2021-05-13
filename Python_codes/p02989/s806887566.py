import math
n=int(input())
a=[int(i) for i in input().split()]
a=sorted(a)
c=(len(a)//2)-1
if(a[c+1]==a[c]):
    print(0)
else:
    print(abs(a[c]-a[c+1]))
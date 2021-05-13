import math
import sys
import collections 
N=int(input())
D = list(map(int, input().split()))
M=int(input())
T = list(map(int, input().split()))
new_D=sorted(D)
new_T=sorted(T)
a=collections.Counter(new_D)
b=collections.Counter(new_T)
#print(a[10])
#print(new_D[0])
for i in new_T:
    if a[i]<b[i]:
        print("NO")
        sys.exit()
    
    
print("YES")
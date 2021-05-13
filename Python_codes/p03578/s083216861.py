import collections
import sys
N=int(input())
D = list(map(int, input().split())) 
M=int(input())
T = list(map(int, input().split())) 
D_count=collections.Counter(D)
T_count=collections.Counter(T)
for i in T:
    if D_count[i]<T_count[i]:
        print("NO")
        sys.exit()
print("YES")
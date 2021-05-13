#import numpy as np
# import math
# import sys
#please work

h,w = map(int, input().split())

l = []
for val in range(h):
    l.append(input())
    
    
ans = [[0 for j in range(w)] for i in range(h)]
#ans = [[0]*w]*
#print(ans)
ans[0][0] =  1

for i in range (h):
    for j in range (w):
        #print(i, j)
        if l[i][j]=="#":
            continue
        if l[i][j] == '.':
            ans[i][j] += (ans[i-1][j] % 1000000007)+(ans[i][j-1] % 1000000007)
print(ans[h-1][w-1] % 1000000007)
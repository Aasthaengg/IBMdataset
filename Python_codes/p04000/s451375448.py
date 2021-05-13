# coding: utf-8
# Your code here!

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
 
#n = int(input())
h,w,n = [int(i) for i in readline().split()]
ab = [[int(i)-1 for i in readline().split()] for _ in range(n)]

ans = [0]*10

#print(ab)
d = {}
for a,b in ab:
    for i in range(3):
        for j in range(3):
            if a-i < 0 or b-j < 0 or a-i >= h-2 or b-j >= w-2: continue
            if (a-i,b-j) in d:
                d[(a-i,b-j)] += 1
            else:
                d[(a-i,b-j)] = 1
        
#print(d)
for i in d.values():
    ans[i] += 1




ans[0] = (h-2)*(w-2) - sum(ans)
print(*ans)








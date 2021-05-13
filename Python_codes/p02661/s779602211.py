import statistics
import math

n = int(input())
aa,bb = [],[]

for i in range(n):
    a,b = map(int,input().split())
    
    aa.append(a)
    bb.append(b)
    
aa.sort()
bb.sort()
    
if n % 2 == 1:
    am = aa[n//2]
    bm = bb[n//2]
    
    ans = bm - am + 1
    
else:
    am = (aa[n//2] + aa[n//2-1]) / 2
    bm = (bb[n//2] + bb[n//2-1]) / 2
    
    ans = (bm - am)*2 + 1
    
print(int(ans))
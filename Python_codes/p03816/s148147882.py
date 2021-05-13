n = int(input())
import collections
co = collections.Counter(map(int,input().split()))
r = 0
for cnt in co.values():
    r+=cnt-1
if r%2==0:
    print(n-r)
else:
    print(n-r-1)  

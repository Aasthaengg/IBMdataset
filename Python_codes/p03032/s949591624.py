from collections import deque

n,k = map(int,input().split())
v = list(map(int,input().split()))

mini = min(n,k)
mx = 0

for a in range(mini+1):
    for b in range(mini+1-a):
        if b==0:
            bb=-n-2
        else:
            bb=b
        ttl = sum(v[:a])+sum(v[-bb:])
        #print(a,b,sum(v[:a]),sum(v[-bb:]))
        hu = [i for i in v[:a] if i<0 ]
        hu.extend([i for i in v[-bb:] if i<0] )
        hu.sort()
        ttl-= sum(hu[:k-a-b])
        mx = max(mx,ttl)
print(mx)

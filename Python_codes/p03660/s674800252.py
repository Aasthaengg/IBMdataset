from heapq import *
n=int(input())
s=[[]for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    s[a].append(b)
    s[b].append(a)
def f(a):
    p=[float("INF")for i in range(n+1)]
    p[a],q=0,[[0,a]]
    while q:
        i,j=heappop(q)
        for w in s[j]:
            if p[w]>i+1:
                p[w]=i+1
                heappush(q,[i+1,w])
    else:
        return p[1:]
s1,t1=f(1),f(n)
a,b=0,0
for i in range(n):
    if s1[i]<=t1[i]:
        a+=1
    else:
        b+=1
print("Fennec" if a>b else "Snuke")
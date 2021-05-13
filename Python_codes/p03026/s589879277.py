import sys
def input():
    return sys.stdin.readline()[:-1]
N=int(input())
s=[[]for i in range(N)]
for i in range(N-1):
    a,b=map(lambda x: int(x)-1,input().split())
    s[a].append(b)
    s[b].append(a)
sys.setrecursionlimit(20000)
l=[None]*N
def hu(n):
    for i in s[n]:
        if l[i]==None:
            l[i]=c.pop()
            hu(i)
c=list(map(int,input().split()))
c.sort()
print(sum(c[:-1]))
l[0]=c.pop()
hu(0)
print(*l)
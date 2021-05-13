n=0
m=input()
c=[0 for i in xrange(m)]
t=[0 for i in xrange(m)]


def d(u):
    global n
    if t[u]:return
    n = n + 1
    t[u]=[u+1,n]
    for i in c[u]:d(i-1)
    n = n + 1
    t[u][2:]=[n]

def dfs():
    for i in range(m):
     l=map(int,raw_input().split())
     c[l[0]-1]=l[2:]
    for i in range(m):
     d(i)
     print " ".join(map(str,t[i]))

dfs()
def d(r):
    global n
    if t[r]:return
    n+=1
    t[r]=[r+1,n]
    for i in c[r]:d(i-1)
    n+=1
    t[r][2:]=[n]
m=input()
c=[0]*m
for _ in range(m):
    l=map(int,raw_input().split())
    c[l[0]-1]=l[2:]
n=0
t=[0]*m
for i in range(m):
    d(i)
    print " ".join(map(str,t[i]))
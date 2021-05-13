n,m = map(int,input().split())

llist = []
rlist = []
for i in range(m):
    l,r = map(int,input().split())
    llist += [l]
    rlist += [r]

print(max(0,min(rlist)-max(llist)+1))

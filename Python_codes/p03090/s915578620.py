def int_raw():
    return int(raw_input())

def ss_raw():
    return raw_input().split()

def ints_raw():
    return map(int,ss_raw())

INF = 1<<29

def make1d_arr(n,val=INF):
    return [val for i in xrange(n)]

def make2d_arr(w,h,val =INF):
    return [[val for i in xrange(w)]for i in xrange(h)]

n = int_raw()

edge = make2d_arr(n,n,0)

n_even = n - n%2

comp_edge = [(i,n_even-i-1) for i in xrange(0,n_even)]

for e in comp_edge:
    edge[e[0]][e[1]]=1
    edge[e[1]][e[0]]=1

m = 0
ans = []

for i in xrange(n):
    for j in xrange(i):
        if edge[j][i] == 0:
            m+=1
            ans.append((i,j))
print m
for a in ans:
    print a[0]+1,a[1]+1

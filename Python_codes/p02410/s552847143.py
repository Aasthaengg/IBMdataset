n, m = map(int, raw_input().split())
a = []
for i in range(n):
    ls2 = map(int, raw_input().split())
    a.append(ls2)
b = []
for i in range(m):
    b.append(input())
c = []
for i in range(n):
    #c.append([])
    #c_pre = []
    c_i = 0
    for j in range(m):
        #c_pre.append(a[i][j]*b[j])
        c_i += a[i][j]*b[j]
    c.append(c_i)
for i in xrange(n):
    print c[i]
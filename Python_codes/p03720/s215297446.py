n,m = map(int,input().split())
a_all = []
b_all = []
for i in range(m):
    a,b = map(int,input().split())
    a_all.append(a-1)
    b_all.append(b-1)
for j in range(n):
    c = list()
    for k in range(m):
        if a_all[k] == j:
            c.append(b_all[k])
        if b_all[k] == j:
            c.append(a_all[k])
    print(len(c))
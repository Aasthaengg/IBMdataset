n,m,l = map(int,input().split())
n_list=[] 
m_list = []
c=[[0 for i in range(l)] for j in range(n)]
for i in range(n):
    n_list.append([int(i) for i in input().split()])
for j in range(m):
    m_list.append([int(i) for i in input().split()])
for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j]+=n_list[i][k]*m_list[k][j]

for i in range(n):
    print(' '.join(str(i) for i in c[i]))

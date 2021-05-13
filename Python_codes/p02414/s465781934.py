n, m ,l= map(int, input().split())

result_vec=[[0]*l for n in range(n)]

a = []
b = []

for i in range(n):
    a.append(list(map(int,input().split())))
    
for i in range(m):
    b.append(list(map(int,input().split())))
    

for i in range(n):
    for j in range(l):
        t=0
        for k in range (m) :
            t+=a[i][k]*b[k][j]
        result_vec[i][j]=t
for n in range(n):
    print(' '.join(map(str,result_vec[n])))   
    

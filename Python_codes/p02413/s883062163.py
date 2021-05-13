r,c=map(int,input().split())
w=[0]*c
q=[]
for i in range(r):
    b=input().split()
    e=[int(s) for s in b]
    q.append(e)
for i in range(r):
    for j in range(c):
        w[j]+=q[i][j]
        print(q[i][j],end=' ')
    print(sum(q[i]))
for j in range(c):
    print(w[j],end=' ')
print(sum(w))

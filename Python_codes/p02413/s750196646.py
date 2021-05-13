r, c = map(int,input().split())
b=[]
for i in range(r):    
        a=list(map(int,input().split()))
        a.append(sum(a))
        b.append(a)
        a=map(str,a)
        print(" ".join(a))
d=[]
for i in range(c+1):
    cs=[]
    for j in range(r):
        cs.append(b[j][i])
    d.append(sum(cs))
d=map(str,d)
print(" ".join(d))
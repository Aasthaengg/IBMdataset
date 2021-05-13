N=int(input())
S=str(input())
m=0
for i in range(N):
    a=[]
    x=S[:i]
    y=S[i:]
    for j in range(len(x)):
        if x[j] in y:
            if x[j] not in a:
                a.append(x[j])
    if len(a)>m:
        m=len(a)
                
print(m)
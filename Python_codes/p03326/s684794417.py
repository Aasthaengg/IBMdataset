n,m=map(int,input().split())
L=[]
for i in range(n):
    L.append(list(map(int,input().split())))
sub=[]
for i in range(3):
    L_i=[]
    for j in range(n):
        L_i.append(sum(L[j])-L[j][i]*2)
    L_i.sort()
    sub.append(sum(L_i[n-m:]))
    sub.append(sum(L_i[:m])*(-1))
    
L_x=[]
for j in range(n):
    L_x.append(sum(L[j]))
L_x.sort()
sub.append(sum(L_x[n-m:]))
sub.append(sum(L_x[:m])*(-1))

print(max(sub))
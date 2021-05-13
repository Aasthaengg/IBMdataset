def m(a,b):
    n=3
    L=[0]*3
    for i in range(n):
        L[i]=a[i]-b[i]
    return L

def f(L):
    return len(set(L))==1

C=[]
for i in range(3):
    C.append(list(map(int,input().split())))

F=True
for i,j in [(0,1),(1,2),(2,0)]:
    F&=f(m(C[i],C[j]))

if F:
    print("Yes")
else:
    print("No")

h,w,k=map(int,input().split())
#a(h,x)
p=[-1]*(w+1)
p[0]=1
p[1]=2
def pat(x):
    if x<0 or x>=w:
        return 1
    else:
        if p[x]!=-1:
            return p[x]
        else:
            p[x]=pat(x-2)+pat(x-1)
            return p[x]
        
for j in range(1):
    0
mo=10**9 +7

a=[[0 for i in range(w)] for i in range(h+1)]
a[0]=[1]+[0]*(w-1)
for i in range(1,h+1):
    #a[i][0]=a[i-1][0]*pat(-1)*pat(h-1)+a[i-1][1]*pat(0)*pat(h-2)
    #a[i][w-1]=a[i-1][w-2]*pat(w-3)*pat(h-w+1)+a[i-1][w-1]*pat(w-1-1)*pat(h-w)
    for j in range(0,w):
        if j>0: a[i][j]+=a[i-1][j-1]*pat(j-2)*pat(w-j-2)
        a[i][j]+=a[i-1][j]*pat(j-1)*pat(w-1-j-1)
        if j<w-1: a[i][j]+=a[i-1][j+1]*pat(j-1)*pat(w-j-3)
print(a[h][k-1] % mo)
#print(a)

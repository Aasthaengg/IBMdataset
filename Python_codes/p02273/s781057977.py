def Rot(vec):
    new=[]
    new+=[vec[0]/2-vec[1]*3**(1/2)/2]
    new+=[vec[0]*3**(1/2)/2+vec[1]/2]
    return(new)

def Add(L):
    dist=[(L[1][0]-L[0][0])/3,(L[1][1]-L[0][1])/3]
    vec1=Rot(dist)
    p1=[2/3*L[0][0]+1/3*L[1][0],2/3*L[0][1]+1/3*L[1][1]]
    p2=[p1[0]+vec1[0],p1[1]+vec1[1]]
    p3=[2/3*L[1][0]+1/3*L[0][0],2/3*L[1][1]+1/3*L[0][1]]
    return([L[0],p1,p2,p3,L[1]])

def Koch(L,n):
    l=len(L)
    if n==0:
        Out=L
    elif n==1:
        if l==2:
            Out=Add(L)
        else:
            L1=L[0:l//2+1]
            L2=L[l//2:l]

            Out=Koch(L1,n)[:-1]+Koch(L2,n)
    else:
        Out=(Koch(Koch(L,n-1),1))

    return(Out)

n=int(input())
L=Koch([[0,0],[100,0]],n)
l=len(L)
for i in range(l):
    print(L[i][0],L[i][1])


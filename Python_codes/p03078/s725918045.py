icase=0
if icase==0:
    x,y,z,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

kk=1

ix=0
iy=0
iz=0
ss=[]
s=a[ix]+b[iy]+c[iz]

xyz=[]
xyz.append((ix+1,iy,iz))
xyz.append((ix,iy+1,iz))
xyz.append((ix,iy,iz+1))

#print(ix,iy,iz,s)
#print(xyz)
ss.append(s)
while kk<k:
    kk+=1
    s1=0
    for ix,iy,iz in xyz:
        s2=a[ix]+b[iy]+c[iz]
        if s2>s1:
            s1=s2
            ixx,iyy,izz=ix,iy,iz
#    print("1:",ixx,iyy,izz,s2)
    xyz.remove((ixx,iyy,izz))
    if ixx<x-1 and ((ixx+1,iyy,izz) not in xyz): 
        xyz.append((ixx+1,iyy,izz))
    if iyy<y-1 and ((ixx,iyy+1,izz) not in xyz): 
        xyz.append((ixx,iyy+1,izz))
    if izz<z-1 and ((ixx,iyy,izz+1) not in xyz): 
        xyz.append((ixx,iyy,izz+1))
#    print(ixx,iyy,izz,s1)
#    print(xyz)
    ss.append(s1)

for kk in range(k):
    print(ss[kk])        

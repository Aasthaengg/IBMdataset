icase=0
if icase==0:
    n,m=map(int,input().split())
    xyz=[[0]*3 for i in range(n)]
    for i in range(n):
        xyz[i]=list(map(int,input().split()))
elif icase==1:
    n,m=5,3
    xyz=[[3, 1, 4], [1, 5, 9], [2, 6, 5], [3, 5, 8], [9, 7, 9]]
elif icase==2:
    n,m=5,3
    xyz=[[1, -2, 3], [-4, 5, -6], [7, -8, -9], [-10, 11, -12], [13, -14, 15]]
elif icase==3:
    n,m=10,5
    xyz=[[10, -80, 21], [23, 8, 38], [-94, 28, 11], [-26, -2, 18], [-69, 72, 79], [-26, -86, -54], [-72, -50, 59], [21, 65, -32], [40, -94, 87], [-62, 18, 82]]
    
import itertools
ic=0
summ=[0]*8    
for j in itertools.product([1,-1], repeat=3):
    xyz0=sorted(xyz,key=lambda x:j[0]*x[0]+j[1]*x[1]+j[2]*x[2],reverse=True)
    for i in range(m):
        summ[ic]+=j[0]*xyz0[i][0]+j[1]*xyz0[i][1]+j[2]*xyz0[i][2]
#    print(ic,xyz0,summ[ic])
    ic+=1
    
print(max(summ))    

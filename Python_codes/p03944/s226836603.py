import sys

def nextrec(coor,pt):
    if pt[2]==1:
        coor[0]=min(max(coor[0],pt[0]),coor[2])
    elif pt[2]==2:
        coor[2]=max(min(coor[2],pt[0]),coor[0])
    elif pt[2]==3:
        coor[1]=min(max(coor[1],pt[1]),coor[3])
    elif pt[2]==4:
        coor[3]=max(min(coor[3],pt[1]),coor[1])
def main(w,h,n,pts):
    rec=[0,0,w,h]
    for x in range(n):
        nextrec(rec,pts[x])
    return (rec[0]-rec[2])*(rec[1]-rec[3])

w,h,n=map(int,sys.stdin.readline().strip().split())
pts=[list(map(int,sys.stdin.readline().strip().split())) \
    for x in range(n)]

print(main(w,h,n,pts))

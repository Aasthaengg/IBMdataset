from sys import stdin
import numpy as np
def main():
    #入力
    readline=stdin.readline
    x1,y1,x2,y2=map(int,readline().split())
    
    p1=np.array([x1,y1])
    p2=np.array([x2,y2])
    R1=np.array([[0,-1],[1,0]])
    R2=np.array([[0,1],[-1,0]])
    p3=np.dot(R2,(p1-p2))+p2
    p4=np.dot(R1,(p2-p1))+p1
    print(p3[0],p3[1],p4[0],p4[1])

if __name__=="__main__":
    main()
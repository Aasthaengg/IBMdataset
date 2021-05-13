#

import sys
input=sys.stdin.readline

def main():
    X,Y,A,B,C=map(int,input().split())
    P=list(map(int,input().split()))
    Q=list(map(int,input().split()))
    R=list(map(int,input().split()))
    lis=[]
    for i in range(A):
        lis.append((P[i],0))
    for i in range(B):
        lis.append((Q[i],1))
    for i in range(C):
        lis.append((R[i],2))
        
    lis.sort(reverse=True)
    white=[]
    sumc=0
    xy=[X,Y]
    for i in range(len(lis)):
        if lis[i][1]==2:
            white.append(lis[i])
        elif xy[lis[i][1]]:
            xy[lis[i][1]]-=1
            sumc+=lis[i][0]
        if (sum(xy)<=len(white)):
            break
    for i in range(len(white)):
        sumc+=white[i][0]
    print(sumc)
            
    
if __name__=="__main__":
    main()

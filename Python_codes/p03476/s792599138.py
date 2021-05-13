# https://atcoder.jp/contests/abc084/tasks/abc084_d

import sys
input=sys.stdin.readline
            
def main():
    sv=[1]*(10**5+1)
    sv[0]=0
    sv[1]=0
    for i in range(int(10**5)+1):
        if sv[i]==0:
            continue
        k=2
        while(k*i<=10**5):
            sv[k*i]=0
            k+=1

    Q=int(input())
    LRs=[tuple(map(int,input().split())) for i in range(Q)]
    like17=[]
    for i in range(1,10**5+1,2):
        if sv[i]!=0 and sv[int((i+1)//2)]!=0:
            like17+=[i]
            
    imo=[0]*(10**5+1)
    for i in range(len(like17)):
        imo[like17[i]+1]=1
    for i in range(10**5):
        imo[i+1]+=imo[i]
    
    for lr in LRs:
        l=lr[0]
        r=lr[1]
        print(imo[r+1]-imo[l])
        
    
if __name__=="__main__":
    main()

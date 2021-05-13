#

import sys
input=sys.stdin.readline

def main():
    N=int(input())
    P=[int(input()) for i in range(N)]
    alr=set()
    iorn=[False]*(N+1)
    for i in range(N):
        if P[i]-1 in alr:
            iorn[P[i]]=True
        alr.add(P[i])
    maxlen=0
    lenn=0
    for i in range(1,N+1):
        if iorn[i]:
            lenn+=1
        else:
            lenn=1
        maxlen=max(maxlen,lenn)
    print(N-maxlen) 
    
    
if __name__=="__main__":
    main()

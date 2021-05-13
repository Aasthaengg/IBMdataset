#

import sys
input=sys.stdin.readline

def main():
    N,A,B=map(int,input().split())
    cnt=0
    for i in range(1,N+1):
        ds=0
        for j in range(5):
            ds+=(int(i//(10**j)))%(10)
        if A<=ds<=B:
            cnt+=i
    print(cnt)
    
if __name__=="__main__":
    main()

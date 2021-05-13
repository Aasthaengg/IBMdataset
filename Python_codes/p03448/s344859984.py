#

import sys
input=sys.stdin.readline

def main():
    A=int(input())
    B=int(input())
    C=int(input())
    X=int(input())
    cnt=0
    for i in range(A+1):
        for j in range(B+1):
            if 0<=X//50-10*i-2*j<=C:
                cnt+=1
    print(cnt)
    
if __name__=="__main__":
    main()

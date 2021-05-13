import sys
import math
import itertools
from functools import reduce
from functools import lru_cache


# \n
def input():
    return sys.stdin.readline().rstrip()

def main():

    N=int(input())
    S=list(input())

    R=[0]*N
    G=[0]*N
    B=[0]*N
    r=0
    g  =0
    b=0
    count =0
    for i in range(N-1,-1,-1):
        if S[i] =="R":
            r+=1
        elif S[i] =="G":
            g+=1
        else:
            b+=1
        R[i]=r
        G[i]=g
        B[i]=b

    count =0
    for i in range(N):



        for j in range(i+1,N):
            SE = set(["R", "G", "B"])
            I = S[i]
            SE.remove(I)
            J =S[j]
            if I==J:
                continue
            SE.remove(J)
            if "G" in SE:
                count+=G[j]
                if j+j-i <N and S[j+j-i] =="G":
                    count -=1

            elif "R" in SE:
                count+=R[j]
                if j+j-i <N and S[j+j-i] =="R":
                    count -=1
            else:
                count+=B[j]
                if j+j-i <N and S[j+j-i] =="B":
                    count -=1



    print(count)


if __name__ == "__main__":
    main()

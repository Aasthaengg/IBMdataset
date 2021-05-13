import numpy as np
import sys

def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    A_double=list(map(lambda x:x//2,A))

    mini_multi=int(np.lcm.reduce(A_double))

    res=M//mini_multi
    
    for i in A_double:
        if (mini_multi//i)%2==0:
            print(0)
            sys.exit()

    if res%2!=0:
        res+=1


    print(res//2)





if __name__=="__main__":
    main()

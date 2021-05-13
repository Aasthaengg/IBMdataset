# https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_d

import sys
input=sys.stdin.readline

def main():
    N=int(input())
    m=0
    k=0
    for i in range(int(((8*N+1)**0.5-1)/2)+1):
        if i*(i+1)==2*N:
            m=i
            k=i+1
            break
    if m==0:
        print("No")
        exit()
    elif N==1:
        print("Yes")
        print(2)
        print(1,1)
        print(1,1)
    else:
        ml=[[] for i in range(k)]
        for i in range(1,k+1):
            ml[i-1].append(str(i))
            ml[i-2].append(str(i))
        for i in range(k+1,N+1):
            ml[(i-k-1)%k].append(str(i))
            l=(i-k-1)//k
            ml[(i-k-1+2+l)%k].append(str(i))
        print("Yes")
        print(k)
        for i in range(k):
            print(m, " ".join(ml[i]))
    
    
if __name__=="__main__":
    main()

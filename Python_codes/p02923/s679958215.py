#

import sys
input=sys.stdin.readline

def main():
    N=int(input())
    H=list(map(int,input().split()))
    H=H[::-1]
    cnt=[0]*N
    for i in range(1,N):
        if H[i]>=H[i-1]:
            cnt[i]=cnt[i-1]+1
    print(max(cnt))
    
    
    
if __name__=="__main__":
    main()

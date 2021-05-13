import math
import copy
import sys
import bisect
input = sys.stdin.readline

def main():
    n=int(input())
    a = list(map(int,input().split()))
    b=[0 for _ in range(n)]
    for i in range(n):
        b[i]=a[i]-i-1
    b.sort()
    if n%2==1:
        mid=b[(n-1)//2]
        ans=0
        for i in range(n):
            ans+=abs(b[i]-mid)
        print(ans)
    else:
        mid = (b[(n//2)-1]+b[(n//2)])//2
        ans=float('inf')
        for i in range(mid,mid+2):
            ans1=0
            for j in range(n):
                ans1+=abs(b[j]-i)
            ans=min(ans1,ans)
        print(ans)

if __name__ == "__main__":
    main()
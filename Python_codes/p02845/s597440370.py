import sys
def input(): return sys.stdin.readline().rstrip()
from collections import Counter
def main():
    n=int(input())
    A=list(map(int,input().split()))
    rgb=[-1,-1,-1]
    ans=1
    mod=10**9+7
    for a in A:
        ans=ans*Counter(rgb)[a-1]%mod
        if ans==0:break
        rgb[rgb.index(a-1)]+=1
    print(ans)
    

if __name__=='__main__':
    main()
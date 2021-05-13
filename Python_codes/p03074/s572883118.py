import sys
from itertools import accumulate
from bisect import bisect_left,bisect_right,insort
#input = sys.stdin.readline

def main():
    n,k=map(int,input().split())
    s=list(input())
    flg,cnt,chk='1',0,[0]    
    for i in range(n):
        if s[i]==flg:
            chk[cnt]+=1
        else:
            flg=str((int(flg)+1)%2)
            cnt+=1
            chk.append(1)
    if s[-1]=='0':
        chk.append(0)
    lng=len(chk)
    if k*2>lng:
        print(n)
    else:
        ans=0
        acc=[0]+list(accumulate(chk))
        for i in range(0,len(chk)-2*k,2):
            ans=max(ans,acc[i+2*k+1]-acc[i])
        print(ans)

if __name__ == '__main__':
    main()
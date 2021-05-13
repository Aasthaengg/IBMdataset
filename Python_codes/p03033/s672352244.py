from bisect import bisect,bisect_left
import sys
input=sys.stdin.readline

def main():
    n,q=map(int,input().split())
    xst=[]
    for i in range(n):
        s,t,x=map(int,input().split())
        xst.append([x,s-x,t-x])
    xst.sort()
    d=[None]*q
    for i in range(q):
        d[i]=int(input())
    ans=[-1]*q
    skip=[-1]*q
    for u in xst:
        x ,left ,right = u
        a=bisect_left(d,left)
        b=bisect_left(d,right)
        while a < b:
            if skip[a] == -1:
                ans[a]=x
                skip[a]=b
                a+=1
            else:
                a=skip[a]
    for u in ans:
        print(u)

if __name__=="__main__":
    main()
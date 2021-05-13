import sys
sys.setrecursionlimit(10**6)
def solve(a,lvl,prev,dp):
    if (prev,lvl) in dp: return dp[(prev,lvl)]
    if lvl==len(a)-1:
        if prev==0: return max(a[-1][1],a[-1][2])
        if prev==1: return max(a[-1][0],a[-1][2])
        if prev==2: return max(a[-1][0],a[-1][1])
    if prev==-1:
        p=a[0][0]+solve(a,lvl+1,0,dp)
        q=a[0][1]+solve(a,lvl+1,1,dp)
        r=a[0][2]+solve(a,lvl+1,2,dp)
        return max(p,q,r)
    dp[(prev,lvl)]=max(a[lvl][(prev+1)%3]+solve(a,lvl+1,(prev+1)%3,dp),a[lvl][(prev-1)%3]+solve(a,lvl+1,(prev-1)%3,dp))
    return dp[(prev,lvl)]
if __name__=='__main__':
    n=int(input())
    a=[]
    for i in range(n):
        a.append([int(i) for i in input().split()])
    if n==1:
        print(max(a[0]))
    else:
        print(solve(a,0,-1,{}))
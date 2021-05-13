from sys import stdin
from itertools import accumulate
def main():
    #入力
    readline=stdin.readline
    n,m,q=map(int,readline().split())
    table=[[0]*n for _ in range(n)]
    for i in range(m):
        l,r=map(lambda x:int(x)-1,readline().split())
        table[l][r]+=1

    #累積和
    for i in range(n):
        table[i]=list(accumulate(table[i]))

    ans=[0]*q
    for i in range(q):
        l,r=map(lambda x:int(x)-1,readline().split())
        t=0
        for j in range(l,r+1):
            t+=table[j][r]
        ans[i]=t

    for i in range(q):
        print(ans[i])

if __name__=="__main__":
    main()
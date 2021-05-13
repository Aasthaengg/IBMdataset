from sys import stdin
import heapq
def main():
    #入力
    readline=stdin.readline
    n,k=map(int,readline().split())
    v=list(map(int,readline().split()))
    v_rev=list(reversed(v))

    m=min(n,k)
    ans=0
    for l in range(m+1):
        for r in range(m+1):
            if l+r>m:
                break

            minus=[]
            s=0
            for i in range(l):
                x=v[i]
                if x<0:
                    minus.append(x)
                s+=x

            for i in range(r):
                x=v_rev[i]
                if x<0:
                    minus.append(x)
                s+=x

            if l+r<k:
                minus.sort()
                for i in range(k-l-r):
                    if i>=len(minus):
                        break
                    s-=minus[i]

            ans=max(ans,s)

    print(ans)

if __name__=="__main__":
    main()
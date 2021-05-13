from sys import stdin
import bisect
def main():
    #入力
    readline=stdin.readline
    inf=10**18
    a,b,q=map(int,readline().split())
    s=[int(readline()) for _ in range(a)]
    s.insert(0,-inf)
    s.append(inf)
    t=[int(readline()) for _ in range(b)]
    t.insert(0,-inf)
    t.append(inf)
    x=[int(readline()) for _ in range(q)]

    for i in range(q):
        j=bisect.bisect_left(s,x[i])
        k=bisect.bisect_left(t,x[i])
        s_i=(s[j-1],s[j])
        t_i=(t[k-1],t[k])
        ans=float("inf")
        for u in s_i:
            for v in t_i:
                ans=min(ans,abs(u-x[i])+abs(v-u))

        for v in t_i:
            for u in s_i:
                ans=min(ans,abs(v-x[i])+abs(u-v))

        print(ans)

if __name__=="__main__":
    main()
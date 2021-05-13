from sys import stdin
def main():
    #入力
    readline=stdin.readline
    h,w,d=map(int,readline().split())
    a=[list(map(int,readline().split())) for _ in range(h)]
    q=int(readline())
    l=[0]*q
    r=[0]*q
    for i in range(q):
        l[i],r[i]=map(int,readline().split())

    #座標メモ
    co=dict()
    for i in range(h):
        for j in range(w):
            co[a[i][j]]=(i,j)

    #累積和
    s=[0]*(h*w+1)
    for i in range(1,d+1):
        j=i+d
        while j<=h*w:
            distance=abs(co[i][0]-co[j][0])+abs(co[i][1]-co[j][1])
            s[j]+=s[i]+distance
            i+=d
            j+=d

    #実技試験
    for i in range(q):
        print(s[r[i]]-s[l[i]])

if __name__=="__main__":
    main()
def main():
    n=int(input())
    xy = sorted([list(map(int, input().split())) for _ in range(n)])
    xy.sort()
    ans=n
    for i in range(n):
        [x1,y1]=xy[i]
        for j in range(n-1):
            [x2,y2]=xy[j]
            if i!=j:
                [p,q]=[x1-x2,y1-y2]
                cnt=0
                for k in range(n-1):
                    for l in range(k+1,n):
                        [x,y]=[ xy[k][0]-xy[l][0],xy[k][1]-xy[l][1] ]
                        if [x,y]==[p,q] or [x,y]==[-p,-q]:
                            cnt+=1
                ans=min(ans,n-cnt)
    print(ans)

if __name__ == "__main__":
    main()
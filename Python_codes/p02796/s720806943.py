from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    xl=[0]*n
    for i in range(n):
        xl[i]=list(map(int,readline().split()))

    a=[[0,0] for _ in range(n)]
    for i in range(n):
        a[i][0]=xl[i][0]-xl[i][1]
        a[i][1]=xl[i][0]+xl[i][1]
    a.sort(key=lambda x:x[1])
    s=a[0][1]
    
    ans=1
    for i in range(1,n):
        if s<=a[i][0]:
            ans+=1
            s=a[i][1]

    print(ans)
    
if __name__=="__main__":
    main()
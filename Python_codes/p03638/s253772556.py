def main():
    h,w=map(int,input().split())
    n=int(input())
    a=list(map(int,input().split()))

    ans=[[0]*w for i in range(h)]
    
    i,j,right=0,0,True
    for color in range(1,n+1):
        #print(ans)
        cnt=a[color-1]
        while cnt>0:
            if right:
                if i+cnt<w:
                    for k in range(i,i+cnt):
                        ans[j][k]=color
                    i+=cnt
                    cnt=0
                else:
                    for k in range(i,w):
                        ans[j][k]=color
                    cnt-=w-i
                    i=w-1
                    j+=1
                    right=False
            
            else:
                if i+1-cnt>0:
                    for k in range(i,i-cnt,-1):
                        ans[j][k]=color
                    i-=cnt
                    cnt=0
                else:
                    for k in range(i,-1,-1):
                        ans[j][k]=color
                    cnt-=i+1
                    i=0
                    j+=1
                    right=True
    for i in range(h):
        print(*ans[i])
if __name__=='__main__':
    main()
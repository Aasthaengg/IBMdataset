def main():
    import sys
    import math
    s,t=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if a[0]<b[0]:
        a,b=b,a
    x=(a[0]-b[0])*s
    y=(a[1]-b[1])*t

    if x+y>0:
        print(0)
        sys.exit()
    elif x+y==0:
        print('infinity')
        sys.exit()

    y=abs(y)
    if x%(y-x)==0: ans=(x//(y-x))*2
    else: ans=math.floor(x/(y-x))*2+1
    print(ans)


 
if __name__ == '__main__':
    main()

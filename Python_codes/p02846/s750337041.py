t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
sa1=(a1-b1)*t1
sa2=(a2-b2)*t2
if sa1>=0:
    sa1*=-1
    sa2*=-1
if sa1+sa2==0:
    print("infinity")
if sa1+sa2<0:
    print(0)
if sa1+sa2>0:
    ans=((-sa1)//(sa2+sa1))*2+1
    if sa1%(sa1+sa2)==0:
        ans-=1
    print(ans)

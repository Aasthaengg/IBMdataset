x,y=map(int,input().split())

ans=abs(x)-abs(y)
#print(ans)
if ans==0:
    if x==y:
        print(ans)
    else:
        print(1)
elif ans<0:
   # print("SDFGH")
    if x<0 and y<0 :
        print(abs(ans)+2)
    elif 0<=x and 0<=y:
        print(abs(ans))
    else:
        print(abs(ans)+1)
else:
    if x<=0 and y<=0:
        print(abs(ans))
    elif 0<x and 0<y:
        print(abs(ans)+2)
    else: 
        
        print(abs(ans)+1)


a,b = map(int,input().split())
#if((a<0 or a>16) or (b<0 or b>16) or (a+b>16)):
    #print("error\n")
count=16
flag=False
pic=0 # 0=a,1=b
while(count>0):
    if(pic==0):
        a-=1
        count-=1
        pic=1    
    elif(pic==1):
        pic=0
        b-=1
        count-=1
    if(a<=0 and b<=0):
        flag=True
        break
if(flag==True):
    print("Yay!")
else:
    print(":(")
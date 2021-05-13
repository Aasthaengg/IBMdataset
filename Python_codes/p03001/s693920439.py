W,H,x,y=map(float,input().split())
num=0
if W==x*2 and H==y*2:
    num=1
print(W*H/2,num)
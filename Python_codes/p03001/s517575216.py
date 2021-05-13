W,H,X,Y=map(int,input().split())

ans2=0
if ((W%2==0)*W//2==X)*(X>0) and ((H%2==0)*H//2==Y)*(Y>0):
    ans2=1

ans1=W*H/2

print(ans1,ans2)
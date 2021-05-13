w,h,x,y=map(int,input().split())
ans1=(w*h)/2.0
ans2=0
if (w/2==x)and(h/2==y):
    ans2=1
print('%f %d'%(ans1,ans2))
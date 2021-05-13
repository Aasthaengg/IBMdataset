x,y=map(int,input().split())
cnt=0
cnt+=y-x
cnt1=1
cnt1+=y+x
cnt2=1
cnt2+=-y-x
cnt3=2
cnt3+=-y+x
a=[cnt,cnt1,cnt2,cnt3]
for i in range(4):
    if a[i]<0:
      a[i]=10000000000000000
print(min(a))
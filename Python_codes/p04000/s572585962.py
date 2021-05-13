h,w,n=map(int,input().split())
d=dict()
def change(a,b):
    global h,w,d
    if 1<=a<h-1 and 1<=b<w-1:
        if (a,b) in d:
            d[(a,b)]+=1
        else:
            d[(a,b)]=1
for i in range(n):
    a,b=map(int,input().split())
    a-=1
    b-=1
    change(a,b)
    change(a-1,b-1)
    change(a-1,b+1)
    change(a+1,b-1)
    change(a+1,b+1)
    change(a-1,b)
    change(a+1,b)
    change(a,b-1)
    change(a,b+1)
ans=[0]*10
ans[0]=(h-2)*(w-2)
#print(d)
for i in d:
    ans[d[i]]+=1
    ans[0]-=1
for i in range(10):
    print(ans[i])


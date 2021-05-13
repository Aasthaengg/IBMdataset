n,h,w=map(int,input().split())
count=0
for i in range(n):
    l,r=map(int,input().split())
    if(l>=h and r>=w):
        count+=1
print(count)
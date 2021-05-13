n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
d=[0]*3
for i in p:
    if i<=a:
        d[0]+=1
    elif a+1<=i<=b:
        d[1]+=1
    elif b+1<=i:
        d[2]+=1
print(min(d))

n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
ca=0
cb=0
cc=0
for i in range(n):
    if p[i]<=a:
        ca+=1
    elif a<p[i] and p[i]<=b:
        cb+=1
    else:
        cc+=1
print(min(ca,cb,cc))
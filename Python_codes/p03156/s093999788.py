n=int(input())
a,b=map(int,input().split())
P=list(map(int,input().split()))
q,w,e=0,0,0
for i in P:
    if i<=a:
        q+=1
    elif i<=b:
        w+=1
    else:
        e+=1
print(min(q,w,e))
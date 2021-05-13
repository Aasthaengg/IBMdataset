from collections import Counter as co
n,m=map(int,input().split())
l=co("".join([input()for i in range(n)])).values()
if n%2 and m%2:
    l=list(l)
    f=1
    for v in range(len(l)):
        if l[v]%2:
            if f:f=0;l[v]-=1
            else:print("No");exit()
    if f==1:print("No");exit()
    print("Yes"if(n+m)//2-1>=len(tuple(1 for j in l if j%4==2)) else "No")
elif (n+m)%2:
    k=(n,m)[n%2]
    print("Yes"if k//2>=len(tuple(1 for j in l if j%4==2)) and 0==len(tuple(1 for j in l if j%2))else"No")
else:print("No"if len(tuple(1 for j in l if j%4))else "Yes")
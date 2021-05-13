a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
if w-v==0:
    if a!=b:
        print("NO")
    else:
        print("YES")
elif -t<=abs(a-b)//(w-v)<=0:
    print("YES")
else:
    print("NO")
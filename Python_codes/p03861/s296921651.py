a,b,x = list(map(int,input().split()))

ans=0
if a!=b:
    A = (a-1)//x
    B = b//x

    ans = B - A
elif a==0 and b==0:
    ans=1
    
elif a==x and b==x:
    ans=1

print(ans)
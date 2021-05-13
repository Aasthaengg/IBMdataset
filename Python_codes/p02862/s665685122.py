x,y=map(int,input().split())
a=max(x,y)
b=min(x,y)
s=a-b
A=a-s-s
if A>=0 and A%3==0:
    t=A//3
    p=t+s
    q=t
    ans=1
    for i in range(q):
        ans=ans*(p+q-i)*pow((i+1),10**9+5,10**9+7)
        ans=ans%(10**9+7)
    print(ans)
else:
    print(0)
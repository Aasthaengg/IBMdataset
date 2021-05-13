N,A,B=map(int,input().split())
x=N//(A+B)
y=N%(A+B)
if y<A:
    ans=x*A+y
else:
    ans=x*A+A
print(ans)

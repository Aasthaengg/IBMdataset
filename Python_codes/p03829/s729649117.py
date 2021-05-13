
n,a,b=map(int,input().split())
x=list(map(int,input().split()))

icnt=0
for i in range(n-1):
    xd=x[i+1]-x[i]
    if b>xd*a:
        icnt+=xd*a
    else:
        icnt+=b
    
print(icnt)

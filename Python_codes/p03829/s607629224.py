n,a,b=map(int,input().split())
x=list(map(int,input().split()))

i=1
cnt=0
while i<n:
    if (x[i]-x[i-1])*a>b:
        cnt+=b
    else:
        cnt+=(x[i]-x[i-1])*a
    i+=1

print(cnt)
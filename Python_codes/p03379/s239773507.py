n=int(input())
x=list(map(int,input().split()))
b=sorted(x)
m=(n-1+1)//2-1
for i in x:
    if i<=b[m]:print(b[m+1])
    else:print(b[m])

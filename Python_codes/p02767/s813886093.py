n=int(input())
x=list(map(int,input().split()))
ans=[]

for i in range(1,101):
    y=0

    for j in range(n):
        y+=(x[j]-i)**2
    ans.append(y)
print(min(ans))
        

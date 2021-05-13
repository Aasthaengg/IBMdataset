n=int(input())
x=list(map(int,input().split()))
y=sorted(x)
ans1=y[(n//2)-1]
ans2=y[n//2]     
for i in range(n):
    if x[i]<=ans1:
        print(ans2)
    else:
        print(ans1)
n,d=list(map(int,input().split()))
count=0
for _ in range(n):
    x,y=list(map(int,input().split()))
    D=pow(pow(x,2)+pow(y,2),0.5)
    if D<=d:
        count+=1
print(count)
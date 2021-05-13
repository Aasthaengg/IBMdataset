x=list(map(int,input().split()))
t=0
for i in range(1,10):
    s=0
    s=x.count(i)
    t+=s
    if s==2:
        print("Yes")
        break
    if t==3:
        print("No")
        break
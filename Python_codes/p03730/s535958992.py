a,b,c=map(int,input().split())

lst=[0]*101
p=a
lst[p]=1
while True:
    if p%b==c:
        print("YES")
        break
    p+=a
    p%=b
    if lst[p]==1:
        print("NO")
        break
    lst[p]=1
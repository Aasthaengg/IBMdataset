a,b,c=map(int,input().split())
flag=0

if a+b==c:
    flag+=1
    print("Yes")

if a==b+c:
    flag+=1
    print("Yes")

if a+c==b:
    flag+=1
    print("Yes")

if flag==0:
    print("No")

a,b,c=map(int,input().split())
k=int(input())
num=0
while a>=b:
    b*=2
    num+=1
    if b>a:
        break
while b>=c:
    c*=2
    num+=1
    if c>b:
        break
if num<=k:
    print("Yes")
else:
    print("No")

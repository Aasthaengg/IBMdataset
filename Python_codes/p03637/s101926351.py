n=int(input())
a=list(map(int,input().split()))
x=[i for i in a if i%4==0]
b=[i for i in a if i%4!=0 and i%2==0]
if len(x)+len(b)//2>=n//2:
    print("Yes")
else:
    print("No")

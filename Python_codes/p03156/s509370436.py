n=int(input())
a,b=map(int,input().split(" "))
p=list(map(int,input().split(" ")))
first=0
second=0
third=0
for i in p:
    if i<=a:
        first+=1
    elif a+1<=i<=b:
        second+=1
    elif i>=b+1:
        third+=1
co=0
while True:
    if first>0 and second>0 and third>0:
        first-=1
        second-=1
        third-=1
        co+=1
    else:
        break
print(co)
n=int(input())
a,b=map(int,input().split())
li=[int(i) for i in input().split()]

under=0
middle=0
upper=0

for i in li:
    if i<=a:
        under+=1
    elif a+1 <=i <= b:
        middle+=1
    else:
        upper+=1
print(min(under,middle,upper))
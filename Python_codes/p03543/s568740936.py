n=int(input())
a=n//1000
b=(n//100)-(a*10)
d=n%10
c=((n%100)-d)//10
if a==b and b==c:
    print("Yes")
elif b==c and c==d:
    print("Yes")
else:
    print("No")

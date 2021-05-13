n=int(input())
a=n%10
b=(n//10)%10
c=(n//100)%10
d=(n//1000)%10
if a==b==c or b==c==d:
    print("Yes")
else:
    print("No")
a=int(input())
if a==1:
    print("Hello World")
else:
    x=(int(input()) for i in range(2))
    print(sum(x))
a,b,c=map(int,input().split())
if int((a+b+c)/a)==2 or int((a+b+c))/b==2 or int((a+b+c))/c==2:
    print("Yes")
else:
    print("No")

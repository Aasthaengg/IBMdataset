a=input()
b=input()
a=a+a[:-1]
if a.find(b)!=-1:
        print("Yes")
else:
        print("No")

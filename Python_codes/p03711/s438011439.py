x=[1,3,5,7,8,10,12]
y=[4,6,9,11]
a=list(map(int,input().split()))
if 2 in a:
    print("No")
elif a[0] in x and a[1] in x:
    print("Yes")
elif a[0] in y and a[1] in y:
    print("Yes")
else:
    print("No")
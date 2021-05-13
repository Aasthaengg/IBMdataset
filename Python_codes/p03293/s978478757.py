a=input()
b=input()
t=0
if len(a)==len(b):
    for i in range(len(a)):
        temp=a[i:]+a[:i]
        if temp==b:
            t=1
            break
if t==0:
    print("No")
else:
    print("Yes")
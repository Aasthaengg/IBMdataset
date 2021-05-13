a = list(map(int,input().split()))
#b = list(map(int,input().split()))
b=int(input())

for i in range(b):
    if a[2]<=a[1]:
        a[2]=2*a[2]
    elif a[1]<=a[0]:
        a[1]=2*a[1]
if a[0]<a[1]<a[2]:
    print("Yes")
else:
    print("No") 

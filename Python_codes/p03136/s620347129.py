n=input()
a=sorted([int(i) for i in input().split()])[::-1]
if a[0]<sum(a[1:]):
    print("Yes")
else:
    print("No")
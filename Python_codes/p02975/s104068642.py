n=int(input())
a=list(map(int,input().split()))
b=a[1]
for i in range(2,n):
    b = b^(a[i])

if b==a[0]:
    print("Yes")
else:
    print("No")
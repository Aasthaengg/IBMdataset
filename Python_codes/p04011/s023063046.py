n=int(input())
k=int(input())
x=int(input())
y=int(input())
pay=0
for i in range(1,n+1):
    if i<=k:
        pay=pay+x
    else:
        pay=pay+y



print(pay)


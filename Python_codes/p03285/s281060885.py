n=int(input())
t=0
for i in range(0,n+1,4):
    if (n-i)%7==0:
        t=1
        break
if t==0:
    print("No")
else:
    print("Yes")
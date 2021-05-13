n=int(input())
*a,=map(int, input().split( ))
b4=0;od=0;
for i in range(n):
    if a[i]%2:
        od+=1
    elif a[i]%4==0:
        b4+=1
if od>b4+1:
    print("No")
elif od==b4+1 and od+b4<n:
    print("No")
else:
    print("Yes")

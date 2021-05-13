n=int(input())
a=list(map(int,input().split()))
c_4=0
c_2=0
for i in range(n):
    if a[i]%4==0:
        c_4+=1
    elif a[i]%2==0:
        c_2+=1
if n%2==0:
    if c_4>=n//2:
        print("Yes")
    else:
        if c_2>=(n-c_4*2):
            print("Yes")
        else:
            print("No")
else:
    if c_4>=n//2:
        print("Yes")
    else:
        if c_2>=(n-c_4*2):
            print("Yes")
        else:
            print("No")
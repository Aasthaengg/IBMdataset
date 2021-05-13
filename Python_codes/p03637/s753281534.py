n=int(input())
a=list(map(int,input().split()))

fcount=0
tcount=0

for i in range(n):
    if a[i]%4==0:
        fcount+=1
    elif a[i]%2==0:
        tcount+=1

ocount=n-(fcount+tcount)

if fcount+tcount>=n:
    print("Yes")
elif ocount<=n//2 and ocount<=fcount:
    print("Yes")
elif n%2!=0 and fcount>=n//2:
    print("Yes")
else:
    print("No")

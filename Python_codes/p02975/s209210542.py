n=int(input())
a=list(map(int,input().split()))
ret=a[0]
for x in range(1,n):
    ret=a[x]^ret
if ret==0:
    print("Yes")
else:
    print("No")
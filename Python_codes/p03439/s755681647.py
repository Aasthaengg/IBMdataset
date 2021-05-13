n=int(input())
print(0)
z=input()[0]
if z=="V":
    exit()
def f(i):
    print(i)
    s=input()[0]
    if s=="V":
        exit()
    if i%2==0:
        if s==z:
            return False
        else:
            return True
    else:
        if s==z:
            return True
        else:
            return False
f(n-1)
left=0
right=n-1
while right-left>1:
    mid=(left+right)//2
    if f(mid):
        right=mid   #ここがleftならansもleft。
    else:
        left=mid
exit()
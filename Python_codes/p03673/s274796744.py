n=int(input())
a=list(map(int,input().split()))
ans=[]
def ap(num1):
    ans.append(num1)
if n%2==0:
    num=n-1
    for i in range(n//2):
        ap(a[num])
        num-=2
    num=0
    for i in range(n//2):
        ap(a[num])
        num+=2
else:
    num=n-1
    for i in range(n//2+1):
        ap(a[num])
        num-=2
    num=1
    for i in range(n//2):
        ap(a[num])
        num+=2
print(*ans)

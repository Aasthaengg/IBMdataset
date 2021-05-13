import sys
sys.setrecursionlimit(10**9)

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

cnt=1
while (a[0]%(2**cnt))==0:
    cnt+=1

cnt-=1
for item in a[1:]:
    if item%(2**cnt)!=0:
        print(0)
        exit()
    if (item//(2**cnt))%2==0:
        print(0)
        exit()


import fractions
ans = a[0]
for i in range(1, n):
    ans = ans * a[i] //fractions.gcd(ans, a[i])

if ans%2==1:
    print(0)
    exit()

if ans//2>m:
    print(0)
    exit()

ans=ans//2

print((((m//ans)*(-1))//2)*(-1))




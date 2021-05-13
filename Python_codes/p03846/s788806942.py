n=int(input())
a=list(map(int,input().split()))
mod=10**9+7
a.sort()

li=[]

for i in range(n-1,-(n),-2):
    li.append(abs(i))

li.sort()

if a==li:
    print((2**(n//2))%mod)
else:
    print(0)
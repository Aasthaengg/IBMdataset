import bisect

n=int(input())
a=sorted(map(int,input().split()))
b=sorted(map(int,input().split()))
c=sorted(map(int,input().split()))

ans=0

for i in range(n):
    num1 = bisect.bisect_left(a,b[i])
    num2 = n - bisect.bisect(c,b[i])
    ans += num1*num2

print(ans)
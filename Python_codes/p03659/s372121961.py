n = int(input())
al = list(map(int, input().split()))

sal=sum(al)
res=10**9+1
temp=0
for i in range(0,n-1):
    temp += al[i]
    res = min(res,abs(sal/2-temp))
    if res <=0.5:
        break

print(int(res*2))
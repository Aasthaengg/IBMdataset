n=int(input())
res=0
for i in range(n):
    x,u=map(str, input().split())
    x=float(x)
    if u =="BTC":x*=380000
    res +=x
print(res)
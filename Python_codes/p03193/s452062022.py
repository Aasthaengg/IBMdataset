n,h,w = map(int,input().split())
res = 0
for i in range(n):
    a,b = map(int,input().split())
    res += a>=h and b>=w
print(res)

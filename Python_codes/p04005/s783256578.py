a,b,c = map(int,input().split())
res = 0
if a*b*c%2!=0:
    res = min([a*b,b*c,c*a])
print(res)

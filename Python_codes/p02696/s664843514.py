a,b,n = map(int, input().split())
if n<b-1:
    x=n
else:
    x=b-1

print((a*x)//b)
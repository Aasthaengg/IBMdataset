
n,a,b=map(int,input().split())
print(min(a,b))
if a+b <= n:
    print('0')
else:
    print((a+b)-n)
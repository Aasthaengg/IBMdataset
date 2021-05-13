n,m = map(int,input().split())

def kai(n):
    u = 1
    for i in range(1,n+1):
        u = (u*(i%(10**9+7)))%(10**9+7)
    return u
        
if abs(n-m)==1:
    print((kai(n)*kai(m))%(10**9+7))
elif n-m==0:
    print((kai(n)*kai(m)*2)%(10**9+7))
else:
    print(0)
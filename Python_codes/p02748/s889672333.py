A,B,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_min=min(a)
b_min=min(b)
discount_m=10000000
for i in range(m):
    x,y,c=map(int,input().split())
    p=a[x-1]+b[y-1]-c
    if p<discount_m:
        discount_m=p
print(min(a_min+b_min,discount_m))

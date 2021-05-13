L,R = map(int,input().split())

if R-L>2019 or L>R :
    print(0)
    exit()
if L%2019+(R-L)>=2019 :
    print(0)
    exit()
l1=L%2019
r1=R%2019

ans = (L*(L+1))%2019
for i in range(L%2019,R%2019+1):
    for j in range(L%2019,R%2019+1):
        if i!=j :
            ans = min( (i*j)%2019, ans)

print( ans )
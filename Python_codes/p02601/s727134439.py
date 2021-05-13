a,b,c=map(int,input().split())
k=int(input())
ans='No'
for _ in range(k):
    if a>=b:
        b*=2
    elif b>=c:
        c*=2
    if a<b<c:
        ans='Yes'
print(ans)
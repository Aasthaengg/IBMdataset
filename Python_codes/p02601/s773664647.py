a,b,c=map(int,input().split())
k=int(input())
for _ in range(k):
    if a>=b:
        b*=2
    else:
        if b>=c:
            c*=2
if a<b<c:
    print("Yes")
else:print("No")
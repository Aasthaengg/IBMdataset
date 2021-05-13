a,b,c=map(int,input().split())
k=int(input())
for _ in range(k):
    if a>=b:
        b*=2
        continue
    else:
        c*=2
if b>a and c>b:
    print("Yes")
else:
    print("No")
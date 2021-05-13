n=int(input())
a=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append((x,y))
ok=False
for i in range(n-2):
    if a[i][0]==a[i][1] and a[i+1][0]==a[i+1][1] and a[i+2][0]==a[i+2][1]:
        ok=True
if ok:
    print("Yes")
else:
    print("No")
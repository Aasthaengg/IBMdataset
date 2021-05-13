n=int(input())
a=list(map(int,input().split()))
a.sort()
t=0
for i in range(1,n):
    if a[i]==a[i-1]:
        t+=1
if t==0:
    print("YES")
else:
    print("NO")
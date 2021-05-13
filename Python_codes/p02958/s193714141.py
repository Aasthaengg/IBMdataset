n=int(input())
p=list(map(int,input().split()))
a=[i for i in range(1,n+1)]
a.sort()
tmp=0
for i in range(n):
    if a[i]!=p[i]:
        tmp+=1
if tmp==0 or tmp==2:
    print("YES")
else:
    print("NO")
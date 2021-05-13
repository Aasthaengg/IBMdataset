n=int(input())
a=[int(i) for i in input().split()]
a.sort()
ch=0
for i in range(1,n):
    if a[i]==a[i-1]:
        ch=1
if ch==1:
    print("NO")
else:
    print("YES")


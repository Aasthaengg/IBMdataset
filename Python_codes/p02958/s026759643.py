n=int(input())
a=[int(x) for x in input().split()]
cnt=0
for i in range(n):
    if a[i]!=i+1:
        cnt+=1
if cnt>2:print("NO")
else:print("YES")
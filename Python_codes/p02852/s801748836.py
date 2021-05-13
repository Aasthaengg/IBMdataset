n,m=[int(j) for j in input().split()]
s=input()[::-1]
l=[]
for i in range(n+1):
    if s[i]=="0":
        l.append(i)
import bisect
ans=[]
c=0
while True:
    if c+m>=n:
        ans.append(n-c)
        break
    p=bisect.bisect_right(l,c+m)-1
    ans.append(l[p]-c)
    if l[p]-c==0:
        print(-1)
        exit()
    c=l[p]
    if c==n:
        break
print(*ans[::-1])



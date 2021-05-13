n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(n):
    c.append((a[i],b[i]))
c=sorted(c,key=lambda x:x[0]-x[1])
x=0
ans = 0
j = 0
for i in range(n):
    if c[i][0]-c[i][1] <0:
        ans += 1
        x += abs(c[i][0]-c[i][1])
    else:
        j=i
        break
for i in range(n-1,j-1,-1):
    if j == 0:
        break
    x-=c[i][0]-c[i][1]
    ans+= 1
    if x<=0:
        break
    
if x<=0:
    print(ans)
else:
    print(-1)
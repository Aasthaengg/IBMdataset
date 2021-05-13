n=int(input())
ans=[]
if n%2==0:
    s=n*(n-1)//2-1
    ss=n*(n+1)//2
    for i in range(1,n):
        t=ss-s-i
        for j in range(i+1,n+1):
            if j!=t:
                ans.append((i,j))
if n%2==1:
    s=n*(n-1)//2
    ss=n*(n+1)//2
    for i in range(1,n):
        t=ss-s-i
        for j in range(i+1,n+1):
            if j!=t:
                ans.append((i,j))
print(len(ans))
for x,y in ans:
    print(x,y)
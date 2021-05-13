n=int(input())
ans=set()
if n%2==0:
    i=1
    while i<n+1-i:
        x,y=i,n+1-i
        for j in range(1,n+1):
            if j!=x and j!=y:
                if (j,x) not in ans:
                    ans.add((x,j))
                if (j,y) not in ans:
                    ans.add((y,j))
        i+=1
else:
    i=1
    while i<n-i:
        x,y=i,n-i
        for j in range(1,n+1):
            if j!=x and j!=y:
                if (j,x) not in ans:
                    ans.add((x,j))
                if (j,y) not in ans:
                    ans.add((y,j))
        i+=1
    for j in range(1,n):
        if (j,n) not in ans:
            ans.add((n,j))
print(len(ans))
for i,j in ans:
    print(i,j)

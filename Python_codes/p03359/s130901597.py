a,b = map(int,input().split())
ans =0
for A in range(1,a+1,1):
    for B in range(1,13,1):
        if A==B:
            if a > A or (a==A and b>=B):
                ans+=1
print(ans)
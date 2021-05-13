n,a,b,c=map(int,input().split())
ans='NO'
if n==1 or a==1 or b==1 or c==1:
    if n==9 or a==9 or b==9 or c==9:
        if n==7 or a==7 or b==7 or c==7:
            if n==4 or a==4 or b==4 or c==4:
                ans='YES'
print(ans)                

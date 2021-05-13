[a,b,c]=list(map(int,input().split()))
ans="NO"
if b-a==c-b:
    ans="YES"
print(ans)
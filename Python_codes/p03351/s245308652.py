a,b,c,d=map(int,input().split())
ans="No"
if abs(a-c)<=d:
    ans="Yes"
elif abs(b-a)<=d and abs(c-b)<=d:
    ans="Yes"
print(ans)
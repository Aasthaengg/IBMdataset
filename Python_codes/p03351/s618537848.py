a,b,c,d = map(int,input().split())
ans = "Yes"
if abs(a-c)>d:
    if not (abs(a-b)<=d and abs(b-c)<=d):
        ans = "No"
print(ans)    
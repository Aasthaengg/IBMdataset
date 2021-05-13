a=list(map(int,input().split()))
ans=0
for i in a:
    ans+=i
if ans<=21:
    print("win")
else:
    print("bust")
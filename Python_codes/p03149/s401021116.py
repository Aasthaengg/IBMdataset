a=list(map(int,input().split()))

ans=False
if len(set(a))==4:
    if 1 in a and 9 in a and 7 in a and 4 in a:
        ans=True
if ans is True:
    print("YES")
else:
    print("NO")
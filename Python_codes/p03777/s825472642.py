a,b=map(str,input().split())
if a=="H":
    if b=="H":
        ans="H"
    elif b=="D":
        ans="D"
elif a=="D":
    if b=="H":
        ans="D"
    elif b=="D":
        ans="H"
print(ans)
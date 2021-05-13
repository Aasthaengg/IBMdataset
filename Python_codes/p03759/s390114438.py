a=sorted([int(i) for i in input().split()])
if a[1]-a[0]==a[2]-a[1]:
    print("YES")
else:
    print("NO")
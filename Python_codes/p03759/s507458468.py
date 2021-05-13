x = sorted(list(map(int,input().split())))

if x[1]-x[0] == x[2]-x[1]:
    print("YES")
else:
    print("NO")
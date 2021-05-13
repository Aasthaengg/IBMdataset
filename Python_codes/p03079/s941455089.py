a,b,c = map(int, input().split())
d = sorted([a,b,c])
if d[0] == d[2]:
    print("Yes")
else:
    print("No")
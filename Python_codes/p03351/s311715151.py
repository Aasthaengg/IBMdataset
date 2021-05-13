a,b,c,d = map(int,input().split())
p = [a,b,c]
p.sort()
if abs(a-c) <= d or (p[2]-p[1] <= d and p[1]-p[0] <= d):
    print("Yes")
else:
    print("No")
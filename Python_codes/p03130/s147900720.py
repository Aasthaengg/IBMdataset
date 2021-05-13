k = []
for i in range(3):
    x,y = map(int,input().split())
    k.append(x)
    k.append(y)
if k.count(1) == 1 and k.count(2) == 2 and k.count(3) == 2 and k.count(4) == 1:
    print("YES")
else:
    print("NO")
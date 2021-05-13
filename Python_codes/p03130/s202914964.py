i = []
for _ in range(3):
    a,b = map(int,input().split())
    i.append(a)
    i.append(b)
if (1 <= i.count(1) and i.count(1) <= 2) and (1 <= i.count(2) and i.count(2) <= 2) and (1 <= i.count(3) and i.count(3) <= 2) and (1 <= i.count(4) and i.count(4) <= 2):
    print ("YES")
else:
    print ("NO")
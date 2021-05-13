check = []
for i in range(3):
    a,b = map(int,input().split())
    check.append(a)
    check.append(b)
if check.count(1) == 1 and check.count(2) == 2 and check.count(3) == 2 and check.count(4) == 1: 
    print("YES")
else:
    print("NO")
l1 = input().split()
a = int(l1[0])
b = int(l1[1])
x = int(l1[2])
if x == a:
    print("YES")
for i in range(1,b+1):
    if x == a+i:
        print("YES")
        exit()
if x < a or (x > (a+b)):
    print("NO")
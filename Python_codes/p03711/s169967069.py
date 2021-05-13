li = [[1,3,5,7,8,10,12],[4,6,9,11],[2]]
x,y = map(int,input().split())
for i in range(3):
    if x in li[i]:
        a = i
for i in range(3):
    if y in li[i]:
        b = i
if a == b:
    print("Yes")
else:
    print("No")

x, y = list(map(int, input().split()))

gA = [1,3,5,7,8,10,12]
gB = [4,6,9,11]
gC = [2]

def ok(x, y, group):
    return (x in group) and (y in group)

if ok(x, y, gA):
    print("Yes")
elif ok(x, y, gB):
    print("Yes")
elif ok(x, y, gC):
    print("Yes")
else:
    print("No")

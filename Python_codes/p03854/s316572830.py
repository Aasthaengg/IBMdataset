s = list(input())

a = list("dream")
b = list("dreamer")
c = list("erase")
d = list("eraser")
flag = 0

while(flag == 0):
    if s[-7:] == b:
        del s[-7:]
    elif s[-6:] == d:
        del s[-6:]
    elif s[-5:] == a or s[-5:] == c:
        del s[-5:]
    elif s == []:
        print("YES")
        flag = 1
    else:
        print("NO")
        flag = 1
l = [int(i) for i in input().split(" ")]
if l[1]%l[0] == 0:
    print(l[0]+l[1])
else:
    print(l[1]-l[0])

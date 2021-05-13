set1 = set([1,3,5,7,8,10,12])
set2 = set([4,6,9,11])
set3 = set([2])

x,y  = map(int, input().split())
x_y = set([x,y])

if x_y<set1:
    print("Yes")
elif x_y<set2:
    print("Yes")
elif x_y<set3:
    print("Yes")
else:
    print("No")
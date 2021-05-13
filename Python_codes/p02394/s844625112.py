X, Y, x, y, r =[int(i) for i in input().split()]
if (0 <= (y-r) and (y+r) <= Y) and (0 <= (x-r) and (x+r) <= X):
    print("Yes")
else:
    print("No")
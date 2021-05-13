xy = list(map(int, input().split())) 
g1 = [1,3,5,7,8,10,12]
g2 = [4,6,9,11]
g3 = [2]
if set(xy) <= set(g1) or set(xy) <= set(g2) or set(xy) <= set(g3):
    print("Yes")
else:
    print("No")
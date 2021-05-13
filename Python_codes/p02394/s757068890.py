W,H,x,y,r = [int(i) for i in input().split()]

if x-r < 0 or x+r > W:
    print("No")

elif y-r < 0 or y+r > H:
    print("No")

elif x < r:
    print("No")

elif y < r:
    print("No")

else:
    print("Yes")
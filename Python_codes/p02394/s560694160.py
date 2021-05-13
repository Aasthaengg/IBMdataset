WHxyr = input()
WHxyr_list = WHxyr.split(" ")
W = int(WHxyr_list[0])
H = int(WHxyr_list[1])
x = int(WHxyr_list[2])
y = int(WHxyr_list[3])
r = int(WHxyr_list[4])

if (x - r >= 0 and y - r >= 0) and (x + r <= W and y + r <= H):
    print("Yes")
else:
    print("No")

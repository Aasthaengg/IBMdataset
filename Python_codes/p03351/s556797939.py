ary = input().split(" ")
a = int(ary[0])
b = int(ary[1])
c = int(ary[2])
d = int(ary[3])

print("Yes") if ((abs(c - a) <= d) or (abs(c - b) <= d and abs(b - a) <= 3)) else print("No")
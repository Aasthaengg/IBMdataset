tmp = input().split(" ")
x = int(tmp[0])
a = int(tmp[1])
b = int(tmp[2])

print("A") if abs(x - a) < abs(x - b) else print("B")
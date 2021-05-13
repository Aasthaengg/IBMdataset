x = input()
y = x.split(" ")
y = [int(z) for z in y]
if y[0] < y[1] and y[1] < y[2]:
    print("Yes")
else:
    print("No")
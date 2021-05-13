a = (int)(input())
b = (int)(input())

ret = 1
for i in range(1, 3+1):
    if i != a and i != b:
        ret = i
        break

print("{}".format(ret))
s = int(input())
v = 1000000000
x = (v-s%v)%v
y = (s+x)//v
print(0, 0, 1000000000, 1, x, y)


s = input().split()

r = int(s[0])
d = int(s[1])
x_i = int(s[2])

for i in range(10):
    x_i = r * x_i - d
    print(x_i)
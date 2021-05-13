v = 100000
for i in range(int(input())):
    v *= 1.05
    if v % 1000 != 0:
        v = v - (v % 1000) + 1000
print(int(v))
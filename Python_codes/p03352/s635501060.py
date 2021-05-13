from math import sqrt
x = int(input())
l = []
if x == 1:
    print(1)
    exit()
for i in range(1, int(sqrt(x))+1):
    for j in range(2, x+1):
        if 1 <= i**j <= x:
            l.append(i**j)
print(max(l))
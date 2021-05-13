import itertools, math
a = [int(input()) for i in range(5)]
x = 130*5
for i in itertools.permutations(a):
    y = 0
    for j in range(4):
        y+=math.ceil(i[j]/10)*10
    y+=i[4]
    x=min(x,y)
print(x)
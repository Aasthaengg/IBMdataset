a, b, c = [int(i) for i in input().split()]

x = max([a,b,c])
tmp = 1
while tmp % 2 == 1:
    tmp = x - a + x - b + x - c
    x += 1

print(tmp // 2)

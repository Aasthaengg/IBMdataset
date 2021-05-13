input = open(0).readline

x = [0]*3
for i in range(3):
    x[i] = int(input().strip())
a, b, h = x[0], x[1], x[2]
ans = int(((a + b) * h)/2)
print(ans)
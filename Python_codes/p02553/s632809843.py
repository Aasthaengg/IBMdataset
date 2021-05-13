a, b, c, d = map(int, input().split())
x = [a*d,a*c,b*c,b*d]
ma =x[0]
for i in range(4):
    if ma<=x[i]:
        ma = x[i]
print(ma)
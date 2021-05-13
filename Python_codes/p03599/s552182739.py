a, b, c, d, e, f = map(int, input().split())
water = []
for i in range(31):
    for j in range(31):
        if (a*i+b*j)*100<=f:
            water.append(a*i+b*j)
water = list(set(water))

result = [[0,a*100,0]]
for i in water:
    for x in range(301):
        for y in range(301):
            if i > 0 and c*x+d*y > 0 and c*x+d*y<=i*e and (c*x+d*y+100*i)<=f:
                result.append([100*(c*x+d*y)/(c*x+d*y+100*i), c*x+d*y+100*i, c*x+d*y])

result.sort(reverse=True)
print(result[0][1], result[0][2])
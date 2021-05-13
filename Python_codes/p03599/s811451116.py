a, b, c, d, e, f = map(int, input().split())
water = []
for i in range(31):
    for j in range(31):
        if a*i+b*j <= f//100:
            water.append(a*i+b*j)
water.pop(water.index(0))
water = list(set(water))
result = [[0,0,0]]
for w in water:
    for i in range(301):
        for j in range(301):
            sugar = c*i+d*j
            if sugar <= w*e and sugar+w*100 <= f: 
                result.append([100*sugar/(sugar+w*100), (sugar+w*100), sugar])
result.sort(reverse=True)
print(result[0][1], result[0][2])
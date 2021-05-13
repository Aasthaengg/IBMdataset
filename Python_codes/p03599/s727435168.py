a,b,c,d,e,f = map(int,(input().split()))

possible_water = []
for i in range(31):
    for j in range(31):
        water = 100*a*i + 100*b*j
        if 0 < water <= f:
            possible_water.append(water)
pw = list(set(possible_water))

possible_sugar = []
for i in range(3001):
    for j in range(3001):
        sugar = c*i + d*j
        if sugar <= f:
            possible_sugar.append(sugar)
ps = list(set(possible_sugar))

ans = []
for i in pw:
    for j in ps:
        if i + j <= f and j <= (i//100)*e:
            c = 100*j/(i+j)
            ans.append([c,i+j,j])

ans.sort(reverse=True)
print(ans[0][1],ans[0][2])
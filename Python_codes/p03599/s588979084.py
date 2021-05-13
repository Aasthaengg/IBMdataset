A,B,C,D,E,F = map(int,input().split())
water = set()
for i in range(0,F+1,100*A):
    for j in range(0,F+1,100*B):
        if i + j <= F:
            water.add(i + j)
water = list(water)
water.sort()
sugar = set()
for i in range(0,F+1,C):
    for j in range(0,F+1,D):
        if i + j <= F:
            sugar.add(i + j)
sugar = list(sugar)
sugar.sort()
#print(water)
#print(sugar)
ans = [[0,100*A,0]]
for i in water:
    for j in sugar:
        if i == 0 or j == 0:
            continue
        if i + j <= F and (i//100)*E >= j:
            #print(i,j)
            ans.append([(100*j)/(i+j),i+j,j])
ans.sort()
#print(ans)
print(ans[-1][1],ans[-1][2])

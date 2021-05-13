A,B,C,D,E,F=map(int,input().split())

best_sugarwater = 100*A
best_sugar = 0
best_con = 0
max_con = E/(100+E)

maxA = F//(100*A)
for i in range(maxA+1):
    maxB = (F-100*A*i)//(100*B)
    for j in range(maxB+1):
        water = 100*A*i+100*B*j
        maxC = (F-100*A*i-100*B*j)//C
        for k in range(maxC+1):
            maxD = (F-100*A*i-100*B*j-C*k)//D
            for l in range (maxD+1):
                sugar = C*k+D*l
                if sugar + water == 0 :
                    pass
                elif (best_con < sugar/(sugar + water) <= max_con ):
                    best_sugarwater = sugar + water
                    best_sugar = sugar
                    best_con = sugar/(sugar + water)

print(best_sugarwater,best_sugar)
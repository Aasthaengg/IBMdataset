A, B, C, D, E, F = map(int, input().split())
dens = 0
ans_water = 100*min(A, B)
ans_sugar = 0
for i in range(31):
    for j in range((F-(100*A*i))//(100*B)+1):
        for k in range((F-(100*A*i)-(100*B*j))//C+1):
            for l in range((F-(100*A*i)-(100*B*j)-(C*k))//D+1):
                water = 100*A*i+100*B*j
                sugar = C*k+D*l
                if water == 0:
                    break
                if sugar <= E*(A*i+B*j):
                    if dens<sugar/(sugar+water):
                        dens = sugar/(sugar+water)
                        ans_water = water
                        ans_sugar = sugar
print(ans_water+ans_sugar, ans_sugar)
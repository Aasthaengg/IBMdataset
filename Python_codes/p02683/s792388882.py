import itertools

dd = list(map(int,input().split()))
NN = dd[0]
MM = dd[1]
XX = dd[2]
success = 0
min_price = 100000*13
arr = [list(map(int,input().split())) for i in range(NN)]
for i in range(1,NN+1):
    comb = list(itertools.combinations(arr,i))
    for j in range(len(comb)):
        total_price = 0
        total_skill = [0]*MM
        doable = [0]*MM
        for k in range(i):
            total_price = total_price + comb[j][k][0]
            for l in range(MM):
                total_skill[l] = total_skill[l] + comb[j][k][l+1]
                if total_skill[l] >= XX:
                    doable[l] = 1
        if min(doable) == 1:
            success = 1
            if total_price < min_price:
                min_price = total_price
if success == 0:
    print(-1)
else:
    print(min_price)
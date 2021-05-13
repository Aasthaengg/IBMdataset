a,b,k = map(int,input().split())
#最大公約数を調べるためa,bのうつ値が最小値のものをsaiに代入
shou = min(a,b)
dai  = max(a,b)
min_list = []

for i in range(1,shou+1):
    if shou % i == 0:
        if dai % i == 0:
            min_list.append(i)

print(min_list[-k])
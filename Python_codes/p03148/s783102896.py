from math import ceil
from collections import defaultdict as dd
n, k = map(int, input().split())
sushi = []
for i in range(n):
    sushi.append(list(map(int, input().split())))
sushi.sort(key=lambda x: x[1])

dic = dd(list)
for sushi_type, oishisa in sushi:
    dic[sushi_type].append(oishisa)

sushi_type_num = len(dic)

#base point priority
dp = [0] * (sushi_type_num + 1)
eaten_sushi = dd(list)
base_point = 0
stack_remove = []
for i in range(k):
    sushi_type, oishisa = sushi.pop()
    eaten_sushi[sushi_type].append(oishisa)
    base_point += oishisa
    if len(eaten_sushi[sushi_type]) >= 2:
        stack_remove.append([sushi_type, oishisa])
bonus_point = len(eaten_sushi) ** 2
point = bonus_point + base_point
dp[len(eaten_sushi)] = point

#print(base_point, bonus_point, eaten_sushi, dp)

while sushi != []:
    #print(base_point, bonus_point, eaten_sushi, dp)
    sushi_type, oishisa = sushi.pop()
    if eaten_sushi[sushi_type] == []:
        #remove
        if stack_remove != []:
            remove_type, remove_oishisa = stack_remove.pop()
            eaten_sushi[remove_type].pop()
            base_point -= remove_oishisa
        #add
            eaten_sushi[sushi_type].append(oishisa)
            base_point += oishisa
            bonus_point = len(eaten_sushi) ** 2
            point = bonus_point + base_point
            dp[len(eaten_sushi)] = point
        else:
            break
print(max(dp))
from itertools import permutations 
a = [int(i) for i in input().split()]
p = permutations(a,3)
mn = 10**10
for i in p:
    cost = 0
    cost += abs(i[0]-i[1])
    cost += abs(i[1]-i[2])
    mn = min(mn,cost)
print(mn)
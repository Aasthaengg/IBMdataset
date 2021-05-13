from itertools import permutations , combinations
a  = list(map(int , input().split()))
p = permutations(a,3)
ans = 999999999
for i in p:
    cost = 0
    for idx in range(1,3):
        cost += abs(i[idx] - i[idx-1])
    ans = min(cost , ans)
print(ans)
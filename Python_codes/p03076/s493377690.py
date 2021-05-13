from itertools import permutations
a = [int(input()) for i in range(5)]
p = permutations(a,5)
ans = 10**9
for l in p:
    now = 0
    for i,item in enumerate(l):
        if i == 4:
            now += item
        else:
            now += item + int(bool(item%10))*10 - item%10
    ans = min(ans,now)
print(ans)

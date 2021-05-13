from itertools import combinations
n = int(input())
i = 1
plus = 1
flg = False
while i <= n:
    if i == n:
        flg = True
        break
    plus += 1
    i += plus
if flg:
    print("Yes")
    res = {i : [] for i in range(plus+1)}
    for i, combi in enumerate(combinations(range(plus + 1), 2), 1):
        res[combi[0]].append(str(i))
        res[combi[1]].append(str(i))
    print(plus + 1)
    for i, val in res.items():
        print(str(plus) + " " + " ".join(val))
else:
    print("No")
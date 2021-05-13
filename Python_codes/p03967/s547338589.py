S = input()
res = len(S) // 2
for st in S:
    res -= int(st == "p")
print(res)
S = list(input())

cntW = 0
res = 0
for i, s in enumerate(S):
    if s == "W":
        res += i - cntW
        cntW += 1

print(res)

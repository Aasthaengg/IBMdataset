S = input()

res = 0
bc = 0
for s in S:
    if s == "B":
        bc += 1
    else:
        res += bc

print(res)
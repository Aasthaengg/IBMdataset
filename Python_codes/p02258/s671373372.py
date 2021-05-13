n = int(input())
maxt = -float("inf")
for i in range(n):
    t = int(input())
    if i == 0:
        mint = t
    else:
        if t - mint > maxt:
            maxt = t - mint
        if t < mint:
            mint = t
print(maxt)

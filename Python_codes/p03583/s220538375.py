x = int(input())

for h in range(1,4000):
    for n in range(1,4000):
        denom = 4/x - 1/h - 1/n
        if denom == 0:
            continue

        w = 1/denom
        if w < 0 or w > 50000:
            continue
        rounded = round(w)
        gosa = w - rounded
        if abs(gosa) < 10**-10:
            print(h,n,rounded)
            exit()
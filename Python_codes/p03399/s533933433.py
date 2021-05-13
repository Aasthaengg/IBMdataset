val = [int(input()) for i in range(4)]
res = []
res.append(val[0]+val[2])
res.append(val[0]+val[3])
res.append(val[1]+val[2])
res.append(val[1]+val[3])

print(min(res))

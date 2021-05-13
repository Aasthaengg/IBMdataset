f = [int(i) for i in input().split() if i.isdigit()]
f.sort()
print(f[0] + f[1])
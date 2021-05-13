s = 0
for i in range(int(input())):
    x, u = input().split()
    if u=='BTC':
        s += float(x)*38*(10**4)
    else:
        s += int(x)
print(s)
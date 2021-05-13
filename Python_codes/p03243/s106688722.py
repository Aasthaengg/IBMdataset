n = int(input())
for i in range(120):
    dum = str(n)
    set_dum = set(dum)
    if 1 == len(set_dum):
        break
    n += 1
print(n)
def nig (x,y):
    if x[0] == y[0]: return -1 if x[1]>y[1] else 1
    return -1 if x[0] < y[0] else 1
cuc_fuk = []
for x in range(input()):
    a,b = raw_input().split()
    cuc_fuk.append((a,int(b),x+1))
for piss in sorted(cuc_fuk, cmp = nig ):
    print piss[2]
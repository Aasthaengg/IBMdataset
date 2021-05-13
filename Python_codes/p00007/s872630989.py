def ceil(src, range):
    k = src / 1000
    if k == int(k):
        return int(src)
    else:
        return ((int)(src / range) + 1 ) * range

debt = 100000
for x in range (0, int(input())):
    debt = ceil(debt * 1.05, 1000)
    
print(int(debt))
(n), *l,  = [list(s.split()) for s in open(0)]

sum_m = 0
for x, y in l:
    # print(x)
    # print(y)
    x = float(x)
    if y == 'JPY':
        sum_m += x
    if y == 'BTC':
        sum_m += (x * 380000.0)
        
print(sum_m)
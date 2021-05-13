n = int(input())
x_s = input()
x = int(x_s, 2)

pops = bin(x).count("1")
x_pop_p = x%(pops + 1)
try:
    x_pop_m = x%(pops - 1)
except:
    x_pop_m = 0
for i in range(0,n):
    if x_s[i] == '1':
        if pops > 1:
            tmp = (x_pop_m - pow(2,n-1-i,(pops - 1)))%(pops - 1)
        else:
            print(0)
            continue
    else:
        tmp = (x_pop_p + pow(2,n-1-i,(pops + 1))) % (pops + 1)
    cnt = 1
    while tmp:
        tmp %= bin(tmp).count("1")
        cnt += 1
    print(cnt)
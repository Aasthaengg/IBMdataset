x = input()

continus_s = 0
living_t_cnt = 0
for i in range(len(x)):
    if x[i] == 'S':
        if continus_s > 0:
            continus_s = 0
        continus_s -= 1
    else:
        continus_s += 1
        if continus_s > 0:
            living_t_cnt += 1
print(living_t_cnt*2)